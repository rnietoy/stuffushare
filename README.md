Stuff You Share
===========

Video sharing website of inspirational stories

Initial Planning
----------------

Setup Web Server
> nginx

> Apache

Database Engine
> Postgre SQL

* Action Item: PostgreSQL vs MySQL investigation

#### Site Memberships - **Angel**
  * Login integration with Facebook

#### Main Page and Page Structure - **Rafa**
  * Grid and Design

#### Video Streaming Uploading/Downloading - **Hugo**
  * Video Player
  * Video Uploader

Revise Video Encoding
> Video encoding - FFmpeg us used to convert between video formats
> Need to convert uploaded videos to a standard format for playing videos

Initial Draft of Video Table to use in the Database

* Id (Primary Key)
* Video Location (File name)
* Owner (Foreign Primary Key)
* Video Name
* Views
* Uploader ip
* Video Likes
* Comments (Foreign Primary Key)

Things to consider
> * Video storage structure
> * Video Uploader
> * Video player
> * TODO: How to create a service in Linux and have it running. If the script crashes the
script/service needs to be relaunched - Python?

###### Workflow
User uploads a video
> Video is transferred to the server's hard drive
>> Job picks video for encoding
>>> After conversion job is done converted video is placed on final destination
>>>> Video becomes visible for all users
>>>>> Done

* To investigate: Cmdline Kung-Fu
