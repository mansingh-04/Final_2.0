# FileOrganizer

**FileOrganizer** is a macOS desktop application that helps you organize files in a folder by their file types. The application sorts your files into separate subfolders based on their extensions (e.g., .txt, .jpg, etc.).

---

## Prerequisites  
- macOS 10.10 (Yosemite) or later 🖥️  
- No installation required. Simply download and run the **.dmg** file 📥

---

## Steps to Install and Run the Application

### **Step 1:**  
Download the **File_2.0** folder from this [link](https://drive.google.com/drive/u/2/folders/11WOmYh30IeXNSfAlKzGjkEVBs-KFukri) 🌐

### **Step 2:**  
- Open the folder and double-click the **File_Manager.dmg** file.  
- Wait for it to open. The application will automatically open the browser and redirect you to the link: [http://127.0.0.1:5000](http://127.0.0.1:5000) 🌍  
- If the file doesn’t open, go to **System Preferences** > **Privacy & Security** 🔒, and allow the app by giving it the necessary permissions.

**Note:**  
- The first time the app opens, it may take a little longer as it installs the required files on your system ⏳

### **Step 3:**  
- **Enter the folder path**: Provide the path of the folder containing the files you want to organize. The app will work with any folder you provide (ensure the folder exists).  
  Example folder path: `/Users/username/Documents/Downloads` 📁
  
- **Click on "Clean Folder"**: The app will organize your files by creating subfolders named after each file type (e.g., **TXT Files**, **JPG Files**, etc.) and move the files accordingly 🔄

---

## Completion  
Once the process is complete, a message will appear on the screen confirming that the folder has been successfully cleaned 🧹

---

## Features  
- Automatically organizes files based on their file extensions 🔀  
- Creates subfolders for each file type (e.g., **TXT Files**, **JPG Files**, etc.) 📂  
- Simple and easy-to-use graphical user interface (GUI) built with Flask 🖱️

---

## Troubleshooting  

### **Error: "Invalid folder path"**  
- Ensure you are entering a valid folder path. You can also drag and drop the folder from Finder into the text input field for convenience 🔍

### **App won’t launch:**  
- Make sure your macOS security settings allow apps from unidentified developers. To do this:  
  1. Go to **System Preferences** > **Security & Privacy** 🔐  
  2. Under the **General** tab, click **Open Anyway** next to the message about **FileOrganizer** 💡
