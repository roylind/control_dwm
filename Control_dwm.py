from ModuleControlProcess import ProcessCriteria, ControlProcesses
from time import sleep
from loguru import logger
logger.add("log_Control_dwm.txt", format="{time} {level} {message}", level="DEBUG", encoding="utf-8")


if __name__ == "__main__":
    try:
        process_for_controlled = ProcessCriteria()
        process_for_controlled.name = "dwm.exe"
        process_for_controlled.max_vms_mb = 20
        controller = ControlProcesses(process_for_controlled)
        while True:
            controller.tick()
            sleep(60)
    except Exception as e:
        logger.exception("")

