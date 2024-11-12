# csc-test

## First Time Setup
find a place in your computer system you like that is kinda organized (~/Documents for example) \
make sure you have git installed (google) \
enter the following in your terminal:
```
// in your chosen directory/folder
https://github.com/EmilyHurn/FloodMap.git
```
## Creating a branch / merge request

tickets from trello will have a number assigned to them, to create and name a branch, follow this convention:
```
git checkout main
git pull
// this ensures you are working off main and not a different merge request
git checkout -b <Ticket#>-<Short-Description>
```
Then, go to github > repo CSCI362 > merge requests, and click on the create merge request at the top.\
Youll want to assign someone to reveiw it and yourself as the assignee,\

## Committing to your merge request
After you have written code, do the following to push it to your branch:
```
git branch
// check if youre on your branch
git status
// see which files you need to add
git add <files you worked on>
git commit
// here you write your commit message. <Ticket#> | detail about what your pushing
git push

// the first time you push, the terminal should yell at you to set upstream
// to main and should provide the line of code you need
```

## Pushing to main
Make sure someone else has reviewed and approved your work and all comments on the merge request are resolved\
Then in the merge request, edit commit message if needed and click merge.
If there is a merge conflict that github can't figure out itself, rebase - I highly recommend using VScode's merge editor
```
git rebase main
// go in VScode to resolve conflicts and save file
git add <file>
git rebase --continue

// do steps until no conflicts remain
```

## rebasing

rebasing is something that happens when there are conflicts while attempting to merge in branches - branch A and branch B both edit the same lines in the same file, so we have to decide how to merge them both into main!

```
//do a git log to determine how many commits your branch has 
git log

// in the text editor pick the oldest commit and squash the rest
// see commits in next window and hit :qw

git rebase -i HEAD~<num of commits>
git push --force

// these prior steps will "squash" together all of the commits on your branch, so you only have to rebase your branch against
// main once instead of rebasing against main for every commit on your branch

// Now, you can start rebasing after all your commits are combined into a single commit
git rebase origin/<branch> (e.g. origin/main)

// use the merge resolver in VScode to handle conflicts
// add files after altering

git rebase --continue

// after rebasing is complete
git push --force
```

