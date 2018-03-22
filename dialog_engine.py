class DialogEngine(object):
    def __init__(self, service_cache, logger, topic_names, subscriberID=APP_ID, pkgPath=PKG_PATH, ASRThreshold=ASR_THRESHOLD):
        #self.language = self.s.ALDialog.getLanguage()
        self.s = service_cache
        self.logger = logger
        self.topic_names = topic_names
        self.subscriberID = subscriberID
        #self.TOPIC_NAME = 'MainMenu'
        self.TOPIC_PATHS = {topic: '{0}/dialog/{1}/{1}_{2}.top'.format(pkgPath, topic, '{}') for topic in self.topic_names}
        #self.TOPIC_PATH = self.TOPIC_PATHS[self.TOPIC_NAME].format(code)
        self.language = "Chinese"
        self.s.ALSpeechRecognition.setLanguage(self.language)
        self.s.ALTextToSpeech.setLanguage(self.language)
        self.s.ALDialog.setLanguage(self.language)
        self.s.ALDialog.setASRConfidenceThreshold(ASRThreshold)
        code = self.s.ALDialog.convertLongToNU(self.language)
        for topic in self.topic_names:
            self.TOPIC_PATH = self.TOPIC_PATHS[topic].format('mnc')
            self.s.ALDialog.loadTopic(self.TOPIC_PATH)
            #self.TOPIC_PATH = self.TOPIC_PATHS[topic].format('enu')
            #self.s.ALDialog.loadTopic(self.TOPIC_PATH)
        try:
            self.s.ALDialog.compileAll()
            self.logger.info("compiled all the topics...")
        except Exception as e:
            self.logger.error(e)
    def stop_current_topic(self):
        self.s.ALTextToSpeech.stopAll()
        self.s.ALAnimatedSpeech._stopAll(True)
        try:
            self.s.ALDialog.unsubscribe(self.subscriberID)
        except:
            self.logger.info("Cannot unsubscribe the dialog: "+self.subscriberID)
        # unload and reload new topics
        topics = self.s.ALDialog.getActivatedTopics()
        for topic in topics:
            self.s.ALDialog.deactivateTopic(topic)
    def restartDialog(self, topic):
        self.stop_current_topic()
        self.startDialog(topic)
    def startDialog(self, topic):
        try:
            self.s.ALDialog.activateTopic(topic)
            self.s.ALDialog.setFocus(topic)
            self.s.ALDialog.subscribe(self.subscriberID)
            self.s.ALDialog.forceOutput()
        except Exception as e:
            self.logger.warning(e)
    def stopDialog(self):
        self.stop_current_topic()
        for topic in self.s.ALDialog.getLoadedTopics("Chinese"):
            self.unload_topic(topic)
       #for topic in self.s.ALDialog.getLoadedTopics("English"):
       #    self.unload_topic(topic)
    @qi.nobind
    def unload_topic(self, topic):
        try:
            self.s.ALDialog.deactivateTopic(topic)
            self.logger.info("Topic {} deactivated".format(topic))
            self.s.ALDialog.unloadTopic(topic, _async=True)
            self.logger.info("Topic {} unloaded".format(topic))
        except Exception as e:
            self.logger.warning("ERROR {}".format(e))