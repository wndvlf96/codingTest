#include "stdafx.h"
#include <opencv/cv.h>
#include <opencv/highgui.h>
 
int main()
{
   
   CvCapture* cap = cvCaptureFromCAM(0);
 
   if (!cap) {
          printf("No Webcam!");
          getchar();
          return 0;
   }
 
   int width = (int)cvGetCaptureProperty(cap, CV_CAP_PROP_FRAME_WIDTH);
   int height = (int)cvGetCaptureProperty(cap, CV_CAP_PROP_FRAME_HEIGHT);    
   IplImage* frame;
  
  
   IplImage* grayImage = cvCreateImage(cvSize(width, height), IPL_DEPTH_8U, 1);
   IplImage* edgeImage = cvCreateImage(cvSize(width, height), IPL_DEPTH_8U, 1);
 
   cvNamedWindow("grayImage", CV_WINDOW_AUTOSIZE);
   cvNamedWindow("edgeImage", CV_WINDOW_AUTOSIZE);
  
   while(1) {
  
          frame = cvQueryFrame(cap);
          if (!frame) break;
         
          cvCvtColor(frame, grayImage, CV_BGR2GRAY);
          cvCanny(grayImage, edgeImage, 50, 100, 3);
 
          cvShowImage("grayImage", grayImage);
          cvShowImage("edgeImage", edgeImage);
          char chKey = cvWaitKey(10);
 
          if (chKey == 27) break; // esc key
   }
 
   cvReleaseCapture(&cap);
   cvReleaseImage(&grayImage);
   cvReleaseImage(&edgeImage);
   cvDestroyAllWindows();
 
   getchar();   
 
   return 0;
}