Warehouse Project
==================

3D models created by the schedule-productions team

----------------------
Development Guideline
-----------------------

1.	Model geometry
2.	Save .blend and export .stl
3.	If the model has unique textures, copy them to the model directory
4.	Create UV map
5.	Export .x
6.	Blender render 500x500 image preview and save
7.	Save .blend copy*
8.	Adjust for CryBlend*
9.	Export Cryengine files*
10.	Use python to create metadata
11.	Send draft model using `cryengine_send_test_model.py`*
12.	Finalize draft model in Cryengine SDK*
13.	Retrieve draft model using `cryengine_retrieve_test_model.py`*
14.	Replace with files from `_retrieve` folder and delete `_retrieve` folder*

(*only necessary for models to use in Cryengine)

-----------------
File Structure
-----------------
> :open_file_folder: 	models
> > :open_file_folder: 		misc
> > > :open_file_folder: 		octocat  
> > > > :gift: 				          octocat.blend  
> > > > :gift:				          octocat_cryengine.blend  
> > > > :triangular_ruler:		  octocat.stl  
> > > > :camera: 			          texture_body.png  
> > > > :camera: 			          texture_eyes.png  
> > > > :globe_with_meridians: 	octocat.x  
> > > > :mag:		 		            preview.png  
> > > > :page_facing_up:		    octocat.cgf  
> > > > :page_facing_up:		    octocat.mtl  
> > > > :page_facing_up:		    octocat.dae  
> > > > :memo:				          meta.txt  
> > > > :large_orange_diamond:  mark_for_cryengine.txt

-----------------------
Using Cryengine Models
-----------------------

> If you wish to use any of the models in a Cryengine project there are some quick changes you must make.  
> `meta.txt` will say whether a given model is Cryengine compatible.

1. Set your cryengine directory by editing `config.txt` and changing the appropriate variable.  
2. Copy `utilities/mark_for_cryengine.txt` to any model folders that you want in your cryengine game directory.  
3. Run `cryengine_library_tool.py` to copy all of the models over.


