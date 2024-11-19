<p align="center">
  <img src="https://capsule-render.vercel.app/api?text=File%20Organizer&animation=fadeIn&type=soft&color=gradient&height=150"/>
</p>

### This project is a file organizer desktop application built using Python and CustomTkinter. It helps users automatically organize files in a specified folder by their file extensions, creating subfolders for each type.

## 🚀 Features

🎉 Organize files in a selected folder based on their extensions.

📂 Creates subfolders for each file type (e.g., `.txt`, `.jpg`, `.pdf`).

📑 Allows users to browse and select the folder to organize.

🔍 Open the selected folder directly from the app after organizing.

## ⚙️ Setup & Installation

Follow these steps to set up and run the File Organizer on your desktop:

1. Clone the repository:

    ```bash
    git clone https://github.com/EmileGreyling/file_organizer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd file_organizer
    ```

3. Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

5. Install required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the application:

    ```bash
    python file_organizer.py
    ```

## 📝 Usage

1. **Browse Folder**: Click the entry box to select a folder to organize.
2. **Organize Files**: Click the "Organize Files" button to organize the files by their extensions.
3. **View the Organized Folder**: Click the "Open Folder" button to open the folder in your file explorer after organizing.

## 🖥️ Compiling as an Executable

To compile the app into an executable:
1. Install **auto-py-to-exe**:

    ```bash
    pip install auto-py-to-exe
    ```

2. Run **auto-py-to-exe** and configure the `.py` script to create an executable for easier access.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make changes, test them, and submit a pull request with explanations.

## 🌟 Improvements

Here are some potential areas for improvement in this project:
- [ ] **Advanced Sorting**: Implement more sophisticated file sorting mechanisms (e.g., by size, date).
- [ ] **Drag and Drop Support**: Allow drag-and-drop functionality to add files or folders.
- [ ] **Error Handling**: Add more robust error handling for invalid folder selections and other issues.
