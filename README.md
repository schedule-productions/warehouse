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

(*only necessary for models to use in Cryengine)

----------------------------------------
Finalizing and Testing Cryengine Models
----------------------------------------
> After doing the steps above, do the following to finalize the model:  
1.	Mark models to draft by copying `utilities/mark_for_cryengine_draft.txt` to model folders  
2.	Send draft models to game directory using `cryengine_send_draft_models.py`  
3.	Finalize draft models in Cryengine SDK  
4.	Retrieve draft models using `cryengine_retrieve_draft_models.py`  
5.	Finalized model files are in `_retrieve` folder of each model folder.  

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


