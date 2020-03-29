# Sets the current dir as a local repo, connects it to a 
# remote repo, and then will push files up to it

git init
git add .
git commit -m "initial commit"
git remote add origin $1
git push -u origin master

echo "Done..."
