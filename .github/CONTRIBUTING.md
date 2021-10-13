# Welcome to the contributing guide

Thank you for showing interest in our project. Any contribution you make means a lot to us and will be reflected in the contributors tab on our repository.

This document will give you a detailed overview over how to contribute to our project and have your Pull Request accepted. Please,make sure you have read through this documentation and followed the correct steps before making your first Pull Request in our repository. If you fail to follow the steps mentioned here, it might lead to your Pull Request being declined.

## Contributors guide

See the [README](https://github.com/DSC-CETB/Py-Scripts/blob/master/README.md) to get an overview of the project and find other necessary information. Here are some great resources to get you comfortable with open source contributions:
- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

<img align="right" width="300" src="https://user-images.githubusercontent.com/64744084/95018364-e7d2df00-067c-11eb-9989-5ed586adb11b.jpg" alt="fork this repository" />

## *Follow These Steps*

## 1️⃣ Fork this repository to your account</br>

- Fork this repository by clicking on the `fork` button on the top of this page.
- This will create a copy of this repository in your account.

## 2️⃣ Clone the Repository

- Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

- Open a terminal and run the following git command:

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/clone.png" alt="clone this repository" />

```shell
git clone https://github.com/DSC-CETB/Py-Scripts.git
```

## 3️⃣ Add a remote (upstream) to original project repository

```shell
cd Py-Scripts
git remote add upstream https://github.com/DSC-CETB/Py-Scripts.git
```

<img align="right" width="300" src="https://firstcontributions.github.io/assets/Readme/copy-to-clipboard.png" alt="copy URL to clipboard" />

## 4️⃣ Now synchronize your forked repo

- It will help you to keep your forked repo updated with the original repo

```shell
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

## 5️⃣ Now create a new branch

- Now create a branch using the `git checkout` command:

```shell
git checkout -b your-new-branch-name
```

_(The name of the branch does not need to have the word add in it, but it's a reasonable thing to include because the purpose of this branch is to add your name to a list.)_

## 6️⃣ Make necessary changes and commit those changes

- Open the folder in your local code editor and add your changes or modifications

- If you go to the project directory and execute the command `git status`, you'll see there are changes.

- After making changes or modification on to your code locally, you need to add these files to the staging area. Add those changes to the branch you just created using the `git add` command:

```shell
git add --all
```

- Once files added, you need to commit the changes to with an appropriate commit message using the `git commit` command:

```shell
git commit -m "<your-message>"
```

## 7️⃣ Push changes to GitHub

* After committing the changes, you need to push the changes to master repo using `git push` command:

```shell
git push origin <your-created-branch-name>
```

replacing `<your-created-branch-name>` with the name of the branch you created earlier.

## 8️⃣ Submit your changes for review

- Once you push the changes to your repository, the Compare & pull request button will appear in **GitHub**.</br>
- Go to your repository on GitHub, you'll see a `Compare & pull request` button. Click on that button

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/compare-and-pull.png" alt="create a pull request" />

- Type a proper description and give the PR an appropriate title. 
- Finally, Open a pull request by clicking the `Create pull request` button.

<img style="float: right;" src="https://firstcontributions.github.io/assets/Readme/submit-pull-request.png" alt="submit pull request" />

Soon we'll be merging all your changes into the master branch of this project. You will get a `notification email` once the changes have been merged.

Congrats! You just completed the standard **fork -> clone -> edit -> pull request** workflow that you'll encounter often as a contributor!
