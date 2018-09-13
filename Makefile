#all: thesis-outline.pdf scheduleForThesis.pdf reviewPres.pdf vivek-jobTalk.pdf vivek-uscTalk.pdf
all: vivek-talk.pdf

TEX_FILES = vthesis.tex thesis.tex defense.tex researchQuestionsAndData.tex sampleSlides.tex vivek-jobTalk.tex listings.tex reviewPres.tex vivek-talk.tex

force:
	rm -f vthesis.pdf thesis.pdf
	make all

listings.pdf: listings.tex
	pdflatex listings.tex

researchQuestionsAndData.pdf: researchQuestionsAndData.tex content_researchQuestionsAndData.tex
	pdflatex researchQuestionsAndData.tex
#	bibtex researchQuestionsAndData
#	pdflatex researchQuestionsAndData.tex
#	pdflatex researchQuestionsAndData.tex

vivek-talk.pdf: vivek-talk.tex
	pdflatex vivek-talk.tex


# The thesis.pdf file is the final version of the thesis. 
thesis.pdf: thesis.tex bibliography.bib
	pdflatex thesis.tex
	bibtex thesis
	pdflatex thesis.tex
	pdflatex thesis.tex

#The vthesis.pdf file contains work on cloud computing and any other additional work not presented in the thesis.pdf. 
vthesis.pdf: vthesis.tex bibliography.bib
	pdflatex vthesis.tex
	bibtex vthesis
	pdflatex vthesis.tex
	pdflatex vthesis.tex


defense.pdf: defense.tex content_defense.tex
	pdflatex defense.tex

defpres.pdf: defpres.tex content_defpres.tex
	pdflatex defpres.tex

#This is the job talk presentation given experience and research done during off period.  
vivek-jobTalk.pdf: vivek-jobTalk.tex content_vivek-jobTalk.tex
	pdflatex vivek-jobTalk.tex

#This is the job talk presentation.
vivek-jobTalk.pdf: vivek-jobTalk.tex content_vivek-jobTalk.tex
	pdflatex vivek-jobTalk.tex

#This is the job talk presentation.
vivek-uscTalk.pdf: vivek-uscTalk.tex content_vivek-uscTalk.tex
	pdflatex vivek-uscTalk.tex

vivek-uscWorkTalk.pdf: vivek-uscWorkTalk.tex content_vivek-uscWorkTalk.tex
	pdflatex vivek-uscWorkTalk.tex

reviewPres.pdf: reviewPres.tex content_reviewPres.tex
	pdflatex reviewPres.tex

jobTalk-outline.pdf: jobTalk-outline.tex
	pdflatex jobTalk-outline.tex

#These are documents to show others organization and time management. This falls under Work:mgmt. 
thesis-outline.pdf: thesis-outline.tex 
	pdflatex thesis-outline.tex

pres-outline.pdf: pres-outline.tex
	pdflatex pres-outline.tex

scheduleForThesis.pdf: scheduleForThesis.tex 
	pdflatex scheduleForThesis.tex

sampleSlides.pdf: sampleSlides.tex content_sampleSlides.tex
	pdflatex sampleSlides.tex

cleanThesis:
	rm -f thesis.aux thesis.toc thesis.log thesis.bbl thesis.blg thesis.pdf 

cleanSlides:
	rm -f researchQuestionsAndData.aux researchQuestionsAndData.toc researchQuestionsAndData.log researchQuestionsAndData.bbl researchQuestionsAndData.blg researchQuestionsAndData.pdf

cleanDefPres: defpres.pdf
	rm -f defpres.aux defpres.toc defpres.log defpres.bbl defpres.blg defpres.pdf 

cleanJobTalk: vivek-jobTalk.pdf
	rm -f defpres.aux defpres.toc defpres.log defpres.bbl defpres.blg vivek-jobTalk.pdf 

cleanTalk: vivek-Talk.pdf
	rm -f vivek-talk.aux vivek-talk.toc vivek-talk.log vivek-talk.bbl vivek-talk.blg vivek-talk.pdf 

cleanUSCTalk: vivek-uscTalk.pdf
	rm -f vivek-uscTalk.aux vivek-uscTalk.toc vivek-uscTalk.log vivek-uscTalk.blg vivek-uscTalk.bbl vivek-uscTalk.pdf

cleanUSCWorkTalk: vivek-uscWorkTalk.pdf
	rm -f vivek-uscWorkTalk.aux vivek-uscWorkTalk.toc vivek-uscWorkTalk.log vivek-uscWorkTalk.blg vivek-uscWorkTalk.bbl vivek-uscWorkTalk.pdf

cleanReviewPres: reviewPres.pdf
	rm -f reviewPres.aux reviewPres.toc reviewPres.log reviewPres.bbl reviewPres.blg reviewPres.pdf 

listings: listings.pdf
	rm -f listings.aux listings.toc listings.log listings.bbl listings.pdf

clean:
	rm -f *.aux *.toc *.log *.bbl *.blg thesis.pdf defense.pdf researchQuestionsAndData.pdf defpres.pdf sampleSlides.pdf listings.pdf pres-outline.pdf thesis-outline.pdf schedulueForThesis.pdf vivek-jobTalk.pdf vivek-uscTalk.pdf vivek-talk.pdf
#TODO: see if old researchQuestionsAndData should go into realclean, or another command.  
realclean:
	rm -f *.aux *.toc *.log *.bbl *.blg vthesis.pdf vthesis.aux vthesis.log vthesis.lot vthesis.toc vthesis.lof thesis.aux thesis.log thesis.lot thesis.toc thesis.lof thesis.pdf defense.pdf researchQuestionsAndData.pdf vthesis.pdf defpres.pdf listings.pdf pres-outline.pdf thesis-outline.pdf scheduleForThesis.pdf reviewPres.pdf vivek-uscTalk.pdf vivek-uscWorkTalk.pdf