import fire

from MusicDownloader_eyeD3 import Music
from MusicDownloader_eyeD3 import set_global


def getPlaylist(id, skip=0, metadata=True):
    url = "http://api.injahow.cn/meting/?type=playlist&id=" + str(id)
    set_global("path", url)
    set_global("skip", skip)
    set_global("metadata", metadata)
    Music()


fire.Fire({"gp": getPlaylist})
