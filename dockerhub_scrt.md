## PUSH IMAGES TO DOCKER HUB THROUGH  GITHUB
1. Opend settings in my Github Repository.
2. Went throught Secrets and Variables.
3. Opend Actions and created your secret name as 
     eg : DOCKERHUB_chakra_USERNAME
4. In secrets added dockerhhub ID
      eg : srichakra769
5. Opend Dockerhub and went through security and created new access token and named it as
    
    eg : chakra_token
6. Copied token

7. Went throught Secrets and Variables in my repo in github created new token
     eg : DOCKERHUB_chakra_TOKEN
8. In secrets added chakra_token
        eg :   chakra_token :
               dckr_pat_xxxxxxxxxxx
9. Made changes to my gitactions.yml
```yaml
        name: Login to Docker Hub
        uses: docker/login-action@v3
        with:
            username: ${{ secrets.DOCKERHUB_CHAKRA_USERNAME }}
            password: ${{ secrets.DOCKERHUB_CHAKRA_TOKEN }}

```
            
9. Pushed my image to dockerhub through github
     
       eg : git push

