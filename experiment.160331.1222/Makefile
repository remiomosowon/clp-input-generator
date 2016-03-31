MAINDIR=1
COPYDIR1=2
COPYDIR2=3
RMRF=rm -rf
GENINPUTFILES=python gen_input_files.py

all:
	$(MAKE) help
help:
	@echo ""
	@echo "clean - remove all generated input files and copied dirs"
	@echo "fresh - remove all old data, generate new input files"
	@echo "run - run experiments with existing data"
	@echo "runfresh - run experiments with fresh data"
	@echo ""
clean:
	echo "Starting cleanup..."
	echo "Removing generated input files from main directory"
	$(RMRF) $(MAINDIR)/*.txt
	echo "Removing output data CSV from main directory"
	$(RMRF) $(MAINDIR)/*.csv
	echo "Removing copied directories"
	$(RMRF) $(COPYDIR1) $(COPYDIR2)
	echo "Remove remaining generated input files"
	$(RMRF) c{60,70,80,90,100}/
	$(RMRF) pc*/
fresh:
	$(MAKE) clean
	echo "Create copies of main dir"
	cp -r $(MAINDIR) $(COPYDIR1)
	cp -r $(MAINDIR) $(COPYDIR2)
	echo "Generate new input files"
	$(GENINPUTFILES)
	echo "Done..."
run:
	( cd $(MAINDIR); ./run_experiments.sh ) &
	( cd $(COPYDIR1); ./run_experiments.sh ) &
	( cd $(COPYDIR2); ./run_experiments.sh ) &
runfresh:
	$(MAKE) fresh
	$(MAKE) run

