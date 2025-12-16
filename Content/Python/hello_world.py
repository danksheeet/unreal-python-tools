import unreal

def main():
    unreal.log("-----------------------------------------")
    unreal.log("Hello from a Python script!")
    unreal.log_warning("This is a warning from Python.")
    unreal.log_error("This is an error from Python.")
    unreal.log("-----------------------------------------")
    
    # Show a dialog
    unreal.EditorDialog.show_message(
        title="Hello World",
        message="Hello from the Script Launcher!",
        message_type=unreal.AppMsgType.OK
    )

if __name__ == "__main__":
    main()
