# detectron2-json-export

## How to use

1. Clone this repository into your local detectron 2 project.

2. Rename the original demo folder in the detectron 2 project to `demo-bak`.

3. Create a soft link named `demo` in detectron 2 project root folder pointing to the demo folder of this project. 

   `cd <Your detectron 2 path>`
   
   `ln -s detectron2-json-export/demo ./`   
   
4. In you detectron 2 project folder, execute `demo/demo.py` with your custromized arguments. (Commands in run_test.sh may guide you to use demo.py)
