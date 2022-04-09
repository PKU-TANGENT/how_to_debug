import debugpy
debugpy.listen(("127.0.0.1",5678))
debugpy.wait_for_client()
import sys
print("---Program Start---")
print("This is a script to test passing cmd args.")
breakpoint()
print("The args are:", sys.argv[1:])