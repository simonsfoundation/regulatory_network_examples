# regulatory_network_examples

Some regulatory network examples presented as Jupyter/IPython notebooks.

You may need passwords to decrypt some data files.
If you see a notebook named `decrypt files using password.ipynb` in a folder
then before running other notebooks in the folder open `decrypt files using password.ipynb`
and follow the instructions in the notebook to decrypt data files.

Once all data has been decrypted most networks can be displayed by opening
the other notebooks and then selecting `Cell --> Run All` in the Jupyter menu.

Click below to launch a binder container instance for this repository
(there will be a short pause while the container initializes):

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/simonsfoundation/regulatory_network_examples)

## Adding more networks to this repository

People with appropriate permissions can add additional networks to this repository
and rebuild the binder infrastructure for running the repository via `mybinder`.
Please only add "small" sets of data to this repository.  Large data sets should be
built either as their own repository with their own binder infrastructure, or if they
are very large they should not use the free binder service because binder is not appropriate
for publishing very large data sets.  The procedure outlined below assumes that
the size of the data and the number of files added is not large.

To add additional networks to this repository and rebuild the binder instance:

- Get Github credentials and permissions to modify this repository (see the Github
documentation and talk to your Github administrator and ask the owners of this repository
for permission).

- Clone this repository onto the machine that has the data you want to publish.

- Verify that you have write access to the repository by 
    - adding your initials to the bottom of this file in the cloned repository,
    - `git add README.md`
    - `git commit -m "testing that I can push a commit"`
    - `git push`
    - if that sequence works, congrats, you have write access.
    - if not, go back to the top and fix the problem.

- Create a new folder in the cloned repository to house the new notebooks and data.

- Copy the notebooks and data and any subfolders into the new folder.

- If you wish to encrypt and password protect the data:
    - copy `./DCsimpAtacNetworks/decrypt files using password.ipynb` into the new folder
    - copy `./DCsimpAtacNetworks/encrypt_files.py` into the new folder
    - `cd` into the new folder.
    - execute `python encrypt_files.py delete MYPASSWORD` where `MYPASSWORD` is your password.

- Now you can commit the new folder into the cloned repository, but to make it
easy to fix things in case there is some problem later, don't push the commit until later.
    - `cd` to the repository top level folder
    - `git add NEWFOLDER`
    - `git commit -m "EXPLANATION OF NEWFOLDER CONTENTS"`
    - **don't push until you check things out**

- Now check that everything works right by using the notebook to decrypt the data
(if you encrypted the data) and running the notebooks in the new folder to make
sure there are no problems.

- If there are problems or something got confused a simple strategy is to
simply delete the cloned repository (since we haven't pushed any important changes)
and start over.

- If everything is okay then `git push` to push your changes to the canonical repository.

### Building the binder infrastructure with your changes

After you modify this repository you must rebuild the binder container
and other data structures using the modified repository for binder to use the new data.

- go to http://mybinder.org/
- type `simonsfoundation/regulatory_network_examples` to identify the repository
- select `requirements.txt` to configure the dependencies.
- don't attach any services
- click **make** my binder

Binder may take up to a half hour to finish building the container and other data structures.
Once it completes click the **launch binder** button and verify that everything works
in the binder context.

## Creating a separate repository for larger data

If you want to add larger data sets for use with binder (that are smaller than about
1G total -- it is not polite to use the free binder service with data sets larger 
than that) then create a repository similar to this one.

- Create the repository using the Github web interface and select the "default README" option.
- Clone the new repository to the machine with the data.
- Add `requirements.txt` to the top level directory to specify the software dependencies:
    - `cp ???/regulatory_network_examples/requirements.txt ???/NEW_REPOSITORY/`
    - `cd ???/NEW_REPOSITORY/`
    - `git add requirements.txt`
    - `git commit -m "add requirements"`
    - `git push`
- Then proceed as described above to add a folder to your new repository.




I hope you like!  ARW (add your initials here)
