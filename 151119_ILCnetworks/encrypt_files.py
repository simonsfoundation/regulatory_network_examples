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

dont_encrypt = ".ipynb .crypt .py ~".split()

def get_encoder(password):
    return ARC4.new(password)

def encrypt(password, directory=".", delete=False):
    for filename in os.listdir(directory):
        doit = os.path.isfile(filename)
        for suffix in dont_encrypt:
            if filename.endswith(suffix):
                doit = False
        if doit:
            outname = filename+".crypt"
            print("encrypting "+filename+" to "+outname)
            encoder = get_encoder(password)
            text = open(filename, "rb").read()
            encrypted = encoder.encrypt(text)
            outfile = open(outname, "wb")
            outfile.write(encrypted)
            outfile.close()
            if delete:
                print("deleting "+filename)
                os.unlink(filename)

def decrypt(password, directory="."):
    for filename in os.listdir(directory):
        if filename.endswith(".crypt"):
            outname = filename[:-6]
            print("decrypting "+filename+" to "+outname)
            encrypted = open(filename, "rb").read()
            encoder = get_encoder(password)
            decrypted = encoder.decrypt(encrypted)
            if os.path.exists(outname):
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
    import threading
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
        print "click"
        t = threading.Timer(0.1, extract)
        t.start()
    def extract():
        print "extracting password..."
        print d.send(jQuery("#pw000").val(), pw_callback)
    def pw_callback(arg):
        print "... password extracted"
        password = arg[0]
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
