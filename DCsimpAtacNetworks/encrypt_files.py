"""
Usage:

Encode using password:
% python encrypt_files.py encode password

Decode using password:
% python encrypt_files.py decode password

Encode files and delete unencrypted files:
# python encrypt_files.py delete password
"""

import os
import glob
from Crypto.Cipher import ARC4
import hashlib

dont_encrypt = ".ipynb .crypt .py ~".split()

def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in os.walk(directory):
        if root != "." and root.split("/")[-1].startswith("."):
            continue
        for filename in files:
            if filename.startswith("."):
                continue
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths

def get_encoder(password):
    return ARC4.new(password)

def signature(text):
    return hashlib.sha1(text).hexdigest()

def encrypt(password, directory=".", delete=False):
    for filename in get_filepaths(directory):
        doit = True
        for suffix in dont_encrypt:
            if filename.endswith(suffix):
                doit = False
        if doit:
            outname = filename+".crypt"
            print("encrypting "+filename+" to "+outname)
            encoder = get_encoder(password)
            text = open(filename, "rb").read()
            encrypted = encoder.encrypt(text)
            sig = signature(text)
            #print (text, encrypted, sig)
            outfile = open(outname, "wb")
            outfile.write(sig+"\n")
            outfile.write(encrypted)
            outfile.close()
            if delete:
                print("deleting "+filename)
                os.unlink(filename)

def decrypt(password, directory="."):
    for filename in get_filepaths(directory):
        if filename.endswith(".crypt"):
            outname = filename[:-6]
            print("decrypting "+filename+" to "+outname)
            infile = open(filename, "rb")
            sig = infile.readline()[:-1]
            encrypted = infile.read()
            encoder = get_encoder(password)
            decrypted = encoder.decrypt(encrypted)
            sig2 = signature(decrypted)
            #print (decrypted, encrypted, sig, sig2)
            if sig != sig2:
                print(filename + " HASH SIGNATURE DOESN'T MATCH.")
            elif os.path.exists(outname):
                text = open(outname, "rb").read()
                if text==decrypted:
                    print("Existing file matches "+outname)
                else:
                    print("EXISTING FILE DOES NOT MATCH "+outname)
            else:
                outfile = open(outname, "wb")
                outfile.write(decrypted)
                outfile.close()
                print("wrote "+outname)

def decrypt_widget():
    import time
    from jp_gene_viz import js_proxy
    js_proxy.load_javascript_support()
    # wait for the js to compile...
    time.sleep(0.5)
    from IPython.display import display
    d = js_proxy.ProxyWidget()
    elt = d.element()
    #display(d)
    window = d.window()
    jQuery = window.jQuery
    d(elt.width("400px").height("100px"))
    d(elt.html("""<input type="password" id="pw000"/> <input id="b000" type="button" value="decrypt files"/> """))
    def click_handler(id, args):
        password = d.evaluate(jQuery("#pw000").val())
        # print("pw="+repr(password))
        decrypt(password)
    callback = d.callback(click_handler, None)
    d(jQuery("#b000").click(callback))
    d.flush()
    #display(d)
    return d

if __name__ == "__main__":
    import sys
    [mode, password] = sys.argv[1:]
    if mode == "encode":
        encrypt(password)
    elif mode == "delete":
        encrypt(password, delete=True)
    elif mode == "decode":
        decrypt(password)
    else:
        print __doc__
