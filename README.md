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

## 📸 App Screenshots

<table>
  <tr>
    <td width="50%" align="center">
      <b>🏠 Homepage</b><br>
      <img src="https://github.com/user-attachments/assets/061296e6-74dd-432f-902d-9bd176e46e1b" width="100%">
    </td>
    <td width="50%" align="center">
      <b>📤 Upload Page</b><br>
      <img src="https://github.com/user-attachments/assets/5dfa22c4-9dd9-4ddb-8792-d9f87c749d6d" width="100%">
    </td>
  </tr>
  <tr>
    <td width="50%" align="center">
      <b>⚙️ Process Page</b><br>
      <img src="https://github.com/user-attachments/assets/0141e432-a5be-4d4a-9c62-f36f90c6fc2e" width="100%">
    </td>
    <td width="50%" align="center">
      <b>⬇️ Download Page</b><br>
      <img src="https://github.com/user-attachments/assets/f0c96fcb-575c-44e7-8642-bb2c675fcbfa" width="100%">
    </td>
  </tr>
</table>









