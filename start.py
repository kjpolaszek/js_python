# -*- coding: utf-8 -*-
import sys, datetime, os, codecs
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDate
from os.path import isfile
from editor import Ui_editor
class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
	self.text = 'Wybierz wpis \n <----'	
	self.setWindowIcon(QtGui.QIcon('./Icon/diary-no2.png'))        
	self.ui = Ui_editor()
        self.ui.setupUi(self)
	self.index = 0
	self.ui.textEdit.setText(self.text)
	self.ui.actionClear.triggered.connect(self.clear)
	self.ui.actionOpen.triggered.connect(self.file_open)
	self.ui.actionSave.triggered.connect(self.file_save)
	self.ui.actionSave_as.triggered.connect(self.file_save_as)		
	self.ui.actionInfo.triggered.connect(self.ShowAboutPopup)	
	self.ui.actionRemove.triggered.connect(self.remove_file)
	self.ui.actionnew_day.triggered.connect(self.next_day)
	self.ui.actionHelp.triggered.connect(self.Help)	
	self.currentDate = QDate.currentDate()	
	self.today = datetime.date.today().strftime('%d-%m-%Y')
	self.today_full = datetime.date.today().strftime('%A %d %B %Y')
	self.ui.label_date.setText('Dzisiaj jest: '+self.today_full.decode('utf-8'))	
    	self.filemodel = QtGui.QFileSystemModel()
	self.filemodel.setFilter(QtCore.QDir.NoDotAndDotDot | QtCore.QDir.Files)
	self.filemodel.sort(3,1)	
	self.ui.listView.setModel(self.filemodel)	
        root_index = self.filemodel.setRootPath('./Data')	
	self.ui.listView.setRootIndex(root_index)
	self.ui.listView.clicked.connect(self.clicked)
	self.ui.listView.activated.connect(self.clicked) 		
	
    def next_day(self):
	file_not_exist = True
	dirname=os.path.join('./Data')
	for f in os.listdir(dirname):
		if f == self.today:
			QtGui.QMessageBox.about(self,'Uwaga !','Dzisiejszy wpis już istnieje'.decode('utf-8'))
			file_not_exist = False
	if file_not_exist:
		plik = codecs.open(os.path.join(dirname,self.today),'w','utf-8')
		plik.write(unicode("Mamy dzisiaj ".decode('utf-8')+str(self.today_full).decode('utf-8')+'\n'))
		plik.close()
		
				
    def clicked(self,index):	
	if self.index <> 0 and self.filename == self.today and isfile(self.filepath) and self.text <> unicode(self.ui.textEdit.toPlainText()) :
	   			self.save()
	self.index = index
	self.filename = self.filemodel.fileName(index)
	self.statusBar().showMessage('Wpis z dnia: %s'.decode('utf-8') %self.filename)  
	self.filepath = self.filemodel.filePath(index)  	
	plik = codecs.open(self.filepath,'r','utf-8')
	self.text = plik.read()
	self.ui.textEdit.setText(self.text)
	plik.close()
    
    def file_open(self):
	filepath = QtGui.QFileDialog.getOpenFileName()
	if isfile(filepath):
	    self.filepath=filepath
	    plik = codecs.open(self.filepath,'r','utf-8')
	    self.text = plik.read()
	    self.ui.textEdit.setText(self.text)
	    plik.close()
	    (filepath, filename) = os.path.split(str(filepath))
	    self.statusBar().showMessage('Otworzony plik: %s'.decode('utf-8') %filename)  
    def save(self):
	    plik = codecs.open(self.filepath,'w','utf-8')
            self.text = self.ui.textEdit.toPlainText()
	    plik.write(unicode(self.text))		
	    plik.close()
    def file_save(self):
       	if self.index == 0:
		self.file_save_as()
	else:
	   if self.filemodel.fileName(self.index) <> self.today:
		QtGui.QMessageBox.about(self,"Tylko do odczytu","Ten wpis jest już tylko do odczytu".decode('utf-8')) 	
	   elif isfile(self.filepath):
	    self.save()
	    self.statusBar().showMessage('Zapisano'.decode('utf-8')) 
	   else:
	    self.file_save_as()
    	    
    def file_save_as(self):
	filepath = QtGui.QFileDialog.getSaveFileName()
	if filepath <> '' :
		self.filepath=filepath        	
		self.save()		
		(filepath, filename) = os.path.split(str(filepath))
		self.statusBar().showMessage('Zapisano jako: %s'.decode('utf-8') %filename)  	    
    
   		
    def clear(self):
	if os.path.getsize(self.filemodel.filePath(self.index)) <> 0:
		reply = QtGui.QMessageBox.question(self, 'Czy na pewno?',
            "Czy na pewno chcesz usunąć zawartość wpisu?".decode('utf-8'),
	    QtGui.QMessageBox.Yes| QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes :
        		self.text = str('')
			self.ui.textEdit.setText(self.text)
			self.file_save()	
	
    def remove_file(self):
	reply = QtGui.QMessageBox.question(self, 'Czy na pewno?',
            "Czy na pewno chcesz usunąć wpis z dnia %s?".decode('utf-8') %self.filemodel.fileName(self.index), 
		QtGui.QMessageBox.Yes| QtGui.QMessageBox.No,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
        	filepath = self.filemodel.filePath(self.index)
		os.remove(filepath)
		self.filepath = ''
		self.text = ''
		self.ui.textEdit.setText(self.text)
    def Help(self):
	QtGui.QMessageBox.about(self, "Pomoc Pamiętnik".decode('utf-8'),
		"""I tu jakiś tekst imformujący o tym jak działa
			


		

		""".decode('utf-8'))
		   
    def ShowAboutPopup(self):		
	QtGui.QMessageBox.about(self, "O programie Pamiętnik".decode('utf-8'),
		"""Program <b>'Pamiętnik'</b>. ver 0.94<BR>
		   Zaprojektowany i stworzony przez:<BR>
		   Karol Polaszek<BR>
		   mail: kjpolaszek@gmail.com""".decode('utf-8'))

    def closeEvent(self, event):
	if self.ui.textEdit.toPlainText() <> self.text:       
		reply = QtGui.QMessageBox.question(self, 'Czy na pewno?',
            "Czy na pewno chcesz zakończyć bez zapisu?".decode('utf-8'), QtGui.QMessageBox.Cancel|
            QtGui.QMessageBox.Discard | QtGui.QMessageBox.Save,
	    QtGui.QMessageBox.Save)
	
		if reply == QtGui.QMessageBox.Discard:
			event.accept()
		elif reply == QtGui.QMessageBox.Save:
			self.file_save()
			event.accept()
		else:
			event.ignore()
	
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
