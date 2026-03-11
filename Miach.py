from pathlib import Path

class VM_Detector:
    def __init__(self, target_name: str):
        self.name = target_name
        print(f"{self.name} initialization complete. \nDetecting a VM...")

        self.target_paths = [
            # Virtual Box
            "C:/Windows/System32/drivers/VBoxMouse.sys",
            "C:/Windows/System32/drivers/VBoxGuest.sys",
            "C:/Windows/System32/drivers/VBoxSF.sys",
            "C:/Windows/System32/drivers/VBoxVideo.sys",

            # VMware
            "C:/Windows/System32/drivers/vmmouse.sys",
            "C:/Windows/System32/drivers/vmusbmouse.sys",
            "C:/Windows/System32/drivers/vmhgfs.sys",
            "C:/Windows/System32/drivers/vmmemctl.sys",
        ]

    def check_files(self) -> bool:

        self.detected_paths = []

        for path in self.target_paths:
            if Path(path).exists():
                self.detected_paths.append(path)

        if self.detected_paths:
            print("The following traces were found:")
            for detected_path in self.detected_paths:
                print(detected_path) 
            return True
        else:
            print("No file-based VM artifacts found.")
            return False
        
    def scan(self) -> bool:
        return self.check_files()
detector = VM_Detector("Miach")

detector.scan()