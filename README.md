## Installation
- download the mini_chamfer_calculator.zip under [releases](https://github.com/Jair-F/mini-chamfer-calculator/releases) and extract in your documents folder
- go inside the mini_chamfer_calculator and edit the `run.bat`
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/414c5eea-7ba3-46de-a6cb-c2034a77710a)
- change the selected path to your path to the documents folder:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/3c1999e0-9eb3-41aa-b4a9-f9406e3b56d5)
- open solidworks and edit the macro `run_macro.swp`
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/44a96758-6bd4-445e-8f2b-c9de85d2285d)
- change the selected path to documents path:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/7bb7123e-8627-4bb0-85aa-d2464d00621b)
- save and close the macro
- right click on a tab in solidworks and select `Customize`:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/70d4a3fa-f776-42b1-b718-7a0595a91243)
- go to `Commands` and then select `Macro`:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/0902ddc4-66e0-4f48-9a67-dc90215ba0ad)
- drag the new macro button into the tab:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/65747516-0d20-4ab6-b547-2f24ca59326f)
- select the macro in the new window and a title:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/3dc45aa3-c39e-442b-895e-5047886523dd)
- the new macro button is ready:
  <br>
  ![image](https://github.com/Jair-F/mini-chamfer-calculator/assets/78746086/c8458b09-e58e-4748-9641-8a92dde43cbf)



## self Installation of packages with script
run the `install_deps.ps1`

if powershell doesnt allow to execute run this command as admin and then try again: `Set-ExecutionPolicy Unrestricted`

run the run.bat command and the tool will work

if you downloaded all dependencies you can move the folder to any directory and just run the run.bat and everything should work as expected