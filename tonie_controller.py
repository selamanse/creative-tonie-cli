#! /usr/bin/env python3
import sys, os, shutil, logging
from tonie_api.api import TonieAPI
from tonie_api.models import Config, CreativeTonie, User

log = logging.getLogger(__name__)
logging.basicConfig(level = logging.INFO)
log.addHandler(logging.NullHandler())

class TonieController:
    def __init__(self, user, pwd):
        self.__user = user
        self.__pwd = pwd
        self.__api=TonieAPI(user, pwd)
        self.__creativeTonies = self.__refreshcreativeTonies() # tonies + households

    def __refreshcreativeTonies(self):
    # returns a dictionary with mapping tonies to households
        creativeTonies = {}
        _hhL = self.__api.get_households()
        for _hh in _hhL:
            _tL = self.__api.get_all_creative_tonies_by_household(_hh)
            for _t in _tL:
                log.info(f'found creative tonie %s in household %s', _t.name, _hh.name)
                creativeTonies[_t.name] = _t
        return creativeTonies

    # upload a given episode to a creative tonie
    def tonieUpload(self, tonie_name, f, title):
        tonie = self.__creativeTonies[tonie_name]
        return self.__api.upload_file_to_tonie(tonie, f, title)

    # delete all content on a tonie
    def wipeTonie(self, tonie_name):    
        tonie = self.__creativeTonies[tonie_name]
        return self.__api.clear_all_chapter_of_tonie(tonie)

    def getChaptersForTonie(self, tonie_name):
        tonie = self.__creativeTonies[tonie_name]
        return tonie.chapters
    
    def printToniesOverview(self):
        log.info("done.")