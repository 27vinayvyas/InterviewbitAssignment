Steps to get the webapp worrking:-


virtualenv venv
source venv/bin/activate
pip install django
cd myproject
python manage.py runserver


Move to the link that appear in the terminal ( 127.0.0.1:8000 ). Its the first page, the page where you can schedule an interview, selecting a participant from the already present participants (participant model is created and some dummy values are added by me) and selecting the start and end date.
If the participant is not already involved on those dates, an instane of the interview model would be created and displayed in the next page, which shows the list of all the scheduled interviews.
From this page, you can click on the edit button corresponding to each interview, and you can edit the interview accept its primary key. 


You can navigate to on ( 127.0.0.1:8000/admin ) to see both the tables and all the instances, both the scheduled interviews and the participants list.
