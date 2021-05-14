### About
This application can query for stock details based on the date
Note: This application is hosted on AWS, to see it in action visit - http://ec2-3-223-158-5.compute-1.amazonaws.com/equity/ (navigate to 'steps to get details section' below to see how to work with it. video demonstarion can be found below)

### Steps to run 

- Make sure to have Docker and Docker- compose installed
    - `docker - https://docs.docker.com/engine/install/`
    - `docker-compose - https://docs.docker.com/compose/install/`

- download source code from git
    - `git@github.com:amoghdatt/98F786F7419C16CA3F903EFD7FD91E2BF3B6157ED52C80B8B30E4ABDBA1DD62C.git`
    - `cd stockfinder`
    - `RUN docker-compose up`

- Run the following commands to populate redis with some historical data
   - `http://localhost:8000/equity/download/110521`
   - `http://localhost:8000/equity/download/100521`
   - `http://localhost:8000/equity/download/070521`

- In your browser open http://localhost:8000/equity/

### Steps to get stock details
- Once in the browser, search for your desired stock name, suggestions will show up, select your stock
- select a desired date
- click Add
- You can view your selections by clicking on 'Selections'
- click on 'Get Details'
- Details of the desired stock will be populated in the table


### Folder Structure
- bhavcopy/api - fetching of details from Redis is exposed as API within this folder
- bhavcopy/vueapp - contains vue code to render frontend
- scripts - some import celery scripts and other shell scripts


### Demo


https://user-images.githubusercontent.com/5645152/117972236-7eb8f580-b348-11eb-87ea-3e790cb71611.mp4



