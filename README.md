# Custom_haarcascade
For mode information 
https://docs.opencv.org/4.2.0/dc/d88/tutorial_traincascade.html

1. Setup the environment 
	# Use requirement.txt file

	# install opencv_annotation toolbox
		opencv_annotation toolbox is used to create the annotation for positive samples whic is available in 3.4.11

		Go to Installation by Using the Pre-built Libraries
		https://sourceforge.net/projects/opencvlibrary/files/opencv-win/

		download the exe fiel for windows
		3.3.11


2. Data preparation 
	# Take positive and negative images to train the model (1:2 positive:Negative or 1:10)


	# create labels for negative class using genrate_negative_label_txt.py file

	# generate annotation for positive file using:
		Write Full path of "opencv_annotation.exe" along with output txt file and input positive folder location 
			>D:/haar_cascade_code/Source_code/opencv/build/x64/vc15/bin/opencv_annotation.exe --annotations=pos.txt --images=positive/

			* mark rectangles with the left mouse button,
			* press 'c' to accept a selection,
			* press 'd' to delete the latest selection,
			* press 'n' to proceed with next image,
			* press 'esc' to stop.


	# generate positive samples from the annotations to get a vector file using opencv_createsamples.exe as shown in below command:
		>D:/haar_cascade_code/Source_code/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos.vec
			here minimum Width and height we want to detect is denoted as -w 24 -h 24 

			-num aurgument is must be larger than total number of rectangle in positive sample such as -num 1000 

			output save vector file name augument as -vec pos.vec

			>D:/haar_cascade_code/Source_code/opencv/build/x64/vc15/bin/opencv_createsamples.exe -info pos.txt -w 24 -h 24 -num 1000 -vec pos1.vec
			Info file name: pos.txt
			Img file name: (NULL)
			Vec file name: pos1.vec
			BG  file name: (NULL)
			Num: 1000
			BG color: 0
			BG threshold: 80
			Invert: FALSE
			Max intensity deviation: 40
			Max x angle: 1.1
			Max y angle: 1.1
			Max z angle: 0.5
			Show samples: FALSE
			Width: 24
			Height: 24
			Max Scale: -1
			RNG Seed: 12345
			Create training samples from images collection...
			pos.txt(106) : parse errorDone. Created 253 samples

3. Model training
	# train the cascade classifier model using opencv_traincascade.exe:
		>D:/haar_cascade_code/Source_code/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -numPos 200 -numNeg 100 -numStages 10 -w 24 -h 24
			Here
			-data cascade/  (Location of output the cascade files)
			-vec pos.vec    (Vector file from data processing stage)
			-bg neg.txt     (negative annotation file from data processing stage)
			-numPos 200     (must be less than number of rectangle we draw)
			-numNeg 100 	(you can consider twise or half of pos sample)
			-numStages 10   (more be better 10 is beeter)
			-w 24 -h 24     (minimum width and height you want to detect)


	# WIth Below additional parameters the performance of model will be improved:
		>D:/haar_cascade_code/Source_code/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -precalcValBufSize 6000 -precalcIdxBufSize 6000 -numPos 200 -numNeg 1000 -numStages 12 -w 24 -h 24 -maxFalseAlarmRate 0.4 -minHitRate 0.999

			As we train the cascade classifer we get the output in terms of FA,HR,NUMBER

			HR  HEAT RATE
			FA FALSE ALARM
			N LAYER NUMBER

			Neg Acceptance ratio 0.0035096
			if after point decimal, we are getting the four zero then model is over trained
			
3. Model testing
	# go to cascade folder and look for .xml file to use to detect the area of interest from the input image
		Use the test.py file to detect the ROI from input images