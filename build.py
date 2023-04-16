import subprocess
import json

def buildImage(arch):
    docker_build = [
        "docker",
        "build",
        "-t",
        f"ubuntu:{arch}",
        f"--platform=linux/{arch}",
        "."
    ]
    return docker_build

def runCommand(arch,app,procs,num):
        docker_run = [
            "docker",
            "run",
            "--platform",
            f"linux/{arch}",
            "--rm",
            "-td",
            "-w",
            "/root",
            "-v",
            "./installerCollections:/root/installers",
            "-v",
            f"./{arch}:/root/{arch}",
            "--name",
            f"linux_{arch}_{num}",
            f"ubuntu:{arch}",
            f"installers/{app}.sh",
            arch,
            procs
        ]
        return docker_run

class Config(object):
    def __init__(self):
        super().__init__()
        self.__withImageBuild = False
        self.__archs = []
        self.__apps = []
        self.__procs : int = 2
    
    def setWithImageBuild(self,switch=False):
        self.__withImageBuild = switch
    
    def setArchs(self,archs):
        self.__archs = archs

    def setApps(self,apps):
        self.__apps = apps

    def setProcs(self,procs):
        self.__procs = procs

    def getWithImageBuild(self):
        return self.__withImageBuild
    
    def getArchs(self):
        return self.__archs
    
    def getApps(self):
        return self.__apps
    
    def getProcs(self):
        return self.__procs

if __name__ == "__main__":
    config = Config()

    with open("config.json") as config_file:
        configData = json.loads(config_file.read())
        config.setWithImageBuild(configData["withImageBuild"])
        config.setArchs(configData["archs"])
        config.setApps(configData["apps"])


    if config.getWithImageBuild():
        pops = []
        for arch in config.getArchs():
            pop = subprocess.Popen(buildImage(arch),stdout=subprocess.DEVNULL)
            pops.append(pop)

        for pop in pops:
            pop.wait()
    
    num = 0
    procs = config.getProcs()
    for app in config.getApps():
        for arch in config.getArchs():
            appName = app["name"]
            subprocess.Popen(runCommand(arch,appName,procs,num),stdout=subprocess.DEVNULL)
            num += 1