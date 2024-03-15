## GIT HUB ACTIONS
1. Created a directory using syntax in postgres-sql

            mkdir -p .github/workflows
2. Created a new file 

            gitactions.md
3. Copied yaml code to file (gitactions.md)

4. Made changes in the code.
 
run-name: ${{ github.actor }} is testing out GitHub Actions
on: [push]
jobs:
  Build-docker-image:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - run: docker build -t myflaskimage .
      - run: docker image ls
      - run: docker tag myflaskimage:latest srichakra769/dockerhub:latest
      - run: docker push srichakra769/dockerhub:latest
