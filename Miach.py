class VM_Detector:
    def __init__(self, target_name: str):
        self.name = target_name
        print(self.name + " has started successfully. \nDetecting a VM...")

    def scan(self) -> bool:
        # ここに関数を書く
        return

detector = VM_Detector("Miach")

detector.scan()