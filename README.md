# 🎬 Video Stabilizer Web App

A web-based video stabilization tool built using **Django** and **OpenCV**. Upload a shaky video, and this app will return a stabilized version using transformation-based motion estimation techniques.

🌐 **Live Demo**: [https://videostabilizer-webapp-project.onrender.com](https://videostabilizer-webapp-project.onrender.com)


## Features

- Upload videos in `.mp4` format  
- Stabilizes video using OpenCV transform-based algorithm  
- Download stabilized output  
- Clean, minimal UI  
- Hosted on Render for free access



## Technologies Used

- Python 3.x  
- Django 5.2  
- OpenCV (cv2)  
- HTML5 / CSS3  
- Render (hosting)  
- Whitenoise (for static files)



## 📁 Project Structure

VIDEO_STABILIZER_WEB/<br>
├── media/<br>
├── stabilizer/<br>
├── static/<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── css/<br>
├── staticfiles/<br>
├── templates/<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── stabilizer/<br>
├── venv/<br>
├── video_stabilizer/<br>
├── db.sqlite3<br>
├── manage.py<br>
├── render.yaml<br>
└── requirements.txt<br>


## 🚀 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/videostabilizer-webapp.git
cd videostabilizer-webapp
```
### 2. Set up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install requirements
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
python manage.py runserver
```








