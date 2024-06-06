# Multi language song lyrics extractor + animator

How to install ffmpeg → 

Let's go through a more detailed guide to ensure FFmpeg is added correctly to the PATH on Windows 11:

### **Steps to Add FFmpeg to PATH on Windows 11**

1. **Download and Extract FFmpeg:**
    - Download the "essentials" build of FFmpeg from gyan.dev.
    - Extract the downloaded zip file to a location on your computer, e.g., **`C:\ffmpeg`**.
    - Ensure the extracted folder contains the **`bin`** directory with **`ffmpeg.exe`**, **`ffplay.exe`**, and **`ffprobe.exe`**.
2. **Open Environment Variables:**
    - Press **`Win + S`**, type **`Environment Variables`**, and select "Edit the system environment variables."
    - In the System Properties window, click on the "Environment Variables" button.
3. **Edit the Path Variable:**
    - In the Environment Variables window, under the "System variables" section, find the variable named **`Path`**. Select it and click "Edit".
4. **Add the FFmpeg Bin Directory to the Path:**
    - In the Edit Environment Variable window, click "New" and add the path to the **`bin`** directory of the extracted FFmpeg folder. For example:
        
        ```makefile
        makefileCopy code
        C:\ffmpeg\bin
        
        ```
        
    - Click "OK" to close all windows.

### **Verify FFmpeg Installation**

1. **Open a New Command Prompt or PowerShell Window:**
    - Press **`Win + S`**, type **`cmd`** or **`powershell`**, and press **`Enter`**.
2. **Check FFmpeg Version:**
    - Run the following command to verify that FFmpeg is correctly installed and accessible from any location:
        
        ```bash
        bashCopy code
        ffmpeg -version
        
        ```
        
    - If FFmpeg is correctly added to your PATH, you should see version information output.

### **Troubleshooting**

If the steps above do not work, ensure the following:

1. **Correct Path:**
    - Verify that the path added to the **`Path`** variable points directly to the **`bin`** directory where **`ffmpeg.exe`** is located. The full path should look something like **`C:\ffmpeg\bin`**.
2. **Environment Variable Changes:**
    - Sometimes, changes to environment variables require restarting the Command Prompt or PowerShell. Ensure any Command Prompt or PowerShell windows are closed and reopened after making the changes.
3. **Windows Restart:**
    - In some cases, restarting your computer can ensure that the changes take effect.
4. **Path Length Limit:**
    - Ensure the PATH variable does not exceed the system path length limit. If it does, remove some unnecessary paths or consider using a different method to add FFmpeg to your PATH.

By following these detailed steps, you should be able to resolve the issue and ensure that FFmpeg is correctly added to your PATH on Windows 11. If the problem persists, feel free to share specific error messages or issues you encounter.