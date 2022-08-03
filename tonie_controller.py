#! /usr/bin/env python3
import sys, os, shutil, logging


sys.path.append('./../tonie_api')
from tonie_api import TonieAPI

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

class TonieController:
    def __init__(self, user, pwd):
        self.__user = user
        self.__pwd = pwd
        self.__api=TonieAPI(user, pwd)
        self.__tonieDict = self.__refreshTonieDict() # tonies + households

    def getTonieIdByName(self, name):
        for t in self.__tonieDict:
            tonie_name = self.__api.households[self.__tonieDict[t]].creativetonies[t].name
            if tonie_name == name:
                return t

    def __refreshTonieDict(self):
    # returns a dictionary with mapping tonies to households
        tonieDict = {}
        _hhL = self.__api.households_update()
        for _hh in _hhL:
            _tL = self.__api.households[_hh].creativetonies_update()
            for _t in _tL:
                log.info(f'found creative tonie %s in household %s', _t, _hh)
                tonieDict[_t] = _hh
        return tonieDict

    def tonieUpload(self, tonie, f, title):
    # upload a given episode to a creative tonie
        hh = self.__tonieDict[tonie]
        return self.__api.households[hh].creativetonies[tonie].upload(f, title)

    def wipeTonie(self, tonie):
    # delete all content on a tonie
        hh = self.__tonieDict[tonie]
        return self.__api.households[hh].creativetonies[tonie].remove_all_chapters()

    def getChaptersForTonie(self, tonie):
        hh = self.__tonieDict[tonie]
        return self.__api.households[hh].creativetonies[tonie].chapters