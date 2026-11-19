# Author: João Gustavo A. Amorim
# Author email: joaogustavoamorim@gmail.com
# Coding date:  jan 2019
# python/black: True

# Imports
import numpy as np
import logging
logger = logging.getLogger(__name__)


# Class implemented to calculus the index
class IndexCalculation:
    """
    # Class Summary
            This algorithm consists in calculating vegetation indices, these
        indices can be used for precision agriculture for example (or remote
        sensing). There are functions to define the data and to calculate the
        implemented indices.

    # Vegetation index
        https://en.wikipedia.org/wiki/Vegetation_Index
        A Vegetation Index (VI) is a spectral transformation of two or more bands
        designed to enhance the contribution of vegetation properties and allow
        reliable spatial and temporal inter-comparisons of terrestrial
        photosynthetic activity and canopy structural variations

    # Information about channels (Wavelength range for each)
        * nir - near-infrared
            https://www.malvernpanalytical.com/br/products/technology/near-infrared-spectroscopy
            Wavelength Range 700 nm to 2500 nm
        * Red Edge
            https://en.wikipedia.org/wiki/Red_edge
            Wavelength Range 680 nm to 730 nm
        * red
            https://en.wikipedia.org/wiki/Color
            Wavelength Range 635 nm to 700 nm
        * blue
            https://en.wikipedia.org/wiki/Color
            Wavelength Range 450 nm to 490 nm
        * green
            https://en.wikipedia.org/wiki/Color
            Wavelength Range 520 nm to 560 nm


    # Implemented index list
            #"abbreviationOfIndexName" -- list of channels used

            #"ARVI2"            --  red, nir
            #"CCCI"             --  red, redEdge, nir
            #"CVI"              --  red, green, nir
            #"GLI"              --  red, green, blue
            #"NDVI"             --  red, nir
            #"BNDVI"            --  blue, nir
            #"redEdgeNDVI"      --  red, redEdge
            #"GNDVI"            --  green, nir
            #"GBNDVI"           --  green, blue, nir
            #"GRNDVI"           --  red, green, nir
            #"RBNDVI"           --  red, blue, nir
            #"PNDVI"            --  red, green, blue, nir
            #"ATSAVI"           --  red, nir
            #"BWDRVI"           --  blue, nir
            #"CIgreen"          --  green, nir
            #"CIrededge"        --  redEdge, nir
            #"CI"               --  red, blue
            #"CTVI"             --  red, nir
            #"GDVI"             --  green, nir
            #"EVI"              --  red, blue, nir
            #"GEMI"             --  red, nir
            #"GOSAVI"           --  green, nir
            #"GSAVI"            --  green, nir
            #"Hue"              --  red, green, blue
            #"IVI"              --  red, nir
            #"IPVI"             --  red, nir
            #"I"                --  red, green, blue
            #"RVI"              --  red, nir
            #"MRVI"             --  red, nir
            #"MSAVI"            --  red, nir
            #"NormG"            --  red, green, nir
            #"NormNIR"          --  red, green, nir
            #"NormR"            --  red, green, nir
            #"NGRDI"            --  red, green
            #"RI"               --  red, green
            #"S"                --  red, green, blue
            #"IF"               --  red, green, blue
            #"DVI"              --  red, nir
            #"TVI"              --  red, nir
            #"NDRE"               --  redEdge, nir

    #list of all index implemented
        #allIndex = ["ARVI2", "CCCI", "CVI", "GLI", "NDVI", "BNDVI", "redEdgeNDVI",
                    "GNDVI", "GBNDVI", "GRNDVI", "RBNDVI", "PNDVI", "ATSAVI",
                    "BWDRVI", "CIgreen", "CIrededge", "CI", "CTVI", "GDVI", "EVI",
                    "GEMI", "GOSAVI", "GSAVI", "Hue", "IVI", "IPVI", "I", "RVI",
                    "MRVI", "MSAVI", "NormG", "NormNIR", "NormR", "NGRDI", "RI",
                    "S", "IF", "DVI", "TVI", "NDRE"]

    #list of index with not blue channel
        #notBlueIndex = ["ARVI2", "CCCI", "CVI", "NDVI", "redEdgeNDVI", "GNDVI",
                         "GRNDVI", "ATSAVI", "CIgreen", "CIrededge", "CTVI", "GDVI",
                         "GEMI", "GOSAVI", "GSAVI", "IVI", "IPVI", "RVI", "MRVI",
                         "MSAVI", "NormG", "NormNIR", "NormR", "NGRDI", "RI", "DVI",
                         "TVI", "NDRE"]

    #list of index just with RGB channels
        #RGBIndex = ["GLI", "CI", "Hue", "I", "NGRDI", "RI", "S", "IF"]
    """

    def __init__(self, red=None, green=None, blue=None, red_edge=None, nir=None):
        logger.error(">>> Entering __init__(red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", red, green, blue, red_edge, nir, extra={"event.action": "__init__", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        self.set_matricies(red=red, green=green, blue=blue, red_edge=red_edge, nir=nir)
        logger.warning("<<< Exiting __init__(red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", red, green, blue, red_edge, nir, extra={"event.action": "__init__", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})

    def set_matricies(self, red=None, green=None, blue=None, red_edge=None, nir=None):
        logger.error(">>> Entering set_matricies(red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", red, green, blue, red_edge, nir, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        if red is not None:
            self.red = red
            logger.debug("set_matricies(self=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s): self.red → %s", self, red, green, blue, red_edge, nir, self.red, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        if green is not None:
            self.green = green
            logger.debug("set_matricies(self=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s): self.green → %s", self, red, green, blue, red_edge, nir, self.green, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        if blue is not None:
            self.blue = blue
            logger.debug("set_matricies(self=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s): self.blue → %s", self, red, green, blue, red_edge, nir, self.blue, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        if red_edge is not None:
            self.redEdge = red_edge
            logger.debug("set_matricies(self=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s): self.redEdge → %s", self, red, green, blue, red_edge, nir, self.redEdge, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        if nir is not None:
            self.nir = nir
        logger.debug("set_matricies(self=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s): self.nir → %s", self, red, green, blue, red_edge, nir, self.nir, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        logger.warning("<<< Exiting set_matricies(red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", red, green, blue, red_edge, nir, extra={"event.action": "set_matricies", "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        return True

    def calculation(
        self, index="", red=None, green=None, blue=None, red_edge=None, nir=None
    ):
        logger.error(">>> Entering calculation(index=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", index, red, green, blue, red_edge, nir, extra={"event.action": "calculation", "logrite.index": index, "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
        """
        performs the calculation of the index with the values instantiated in the class
        :str index: abbreviation of index name to perform
        """
        self.set_matricies(red=red, green=green, blue=blue, red_edge=red_edge, nir=nir)
        funcs = {
            "ARVI2": self.arv12,
            "CCCI": self.ccci,
            "CVI": self.cvi,
            "GLI": self.gli,
            "NDVI": self.ndvi,
            "BNDVI": self.bndvi,
            "redEdgeNDVI": self.red_edge_ndvi,
            "GNDVI": self.gndvi,
            "GBNDVI": self.gbndvi,
            "GRNDVI": self.grndvi,
            "RBNDVI": self.rbndvi,
            "PNDVI": self.pndvi,
            "ATSAVI": self.atsavi,
            "BWDRVI": self.bwdrvi,
            "CIgreen": self.ci_green,
            "CIrededge": self.ci_rededge,
            "CI": self.ci,
            "CTVI": self.ctvi,
            "GDVI": self.gdvi,
            "EVI": self.evi,
            "GEMI": self.gemi,
            "GOSAVI": self.gosavi,
            "GSAVI": self.gsavi,
            "Hue": self.hue,
            "IVI": self.ivi,
            "IPVI": self.ipvi,
            "I": self.i,
            "RVI": self.rvi,
            "MRVI": self.mrvi,
            "MSAVI": self.m_savi,
            "NormG": self.norm_g,
            "NormNIR": self.norm_nir,
            "NormR": self.norm_r,
            "NGRDI": self.ngrdi,
            "RI": self.ri,
            "S": self.s,
            "IF": self._if,
            "DVI": self.dvi,
            "TVI": self.tvi,
            "NDRE": self.ndre,
        }

        try:
            return funcs[index]()
        except KeyError:
            print("Index not in the list!")
            logger.warning("<<< Exiting calculation(index=%s,red=%s,green=%s,blue=%s,red_edge=%s,nir=%s)", index, red, green, blue, red_edge, nir, extra={"event.action": "calculation", "logrite.index": index, "logrite.red": red, "logrite.green": green, "logrite.blue": blue, "logrite.red_edge": red_edge, "logrite.nir": nir})
            return False

    def arv12(self):
        """
        Atmospherically Resistant Vegetation Index 2
        https://www.indexdatabase.de/db/i-single.php?id=396
        :return: index
            -0.18+1.17*(self.nir-self.red)/(self.nir+self.red)
        """
        logger.error(">>> Entering arv12()", extra={"event.action": "arv12"})
        logger.warning("<<< Exiting arv12()", extra={"event.action": "arv12"})
        return -0.18 + (1.17 * ((self.nir - self.red) / (self.nir + self.red)))

    def ccci(self):
        """
        Canopy Chlorophyll Content Index
        https://www.indexdatabase.de/db/i-single.php?id=224
        :return: index
        """
        logger.error(">>> Entering ccci()", extra={"event.action": "ccci"})
        logger.warning("<<< Exiting ccci()", extra={"event.action": "ccci"})
        return ((self.nir - self.redEdge) / (self.nir + self.redEdge)) / (
            (self.nir - self.red) / (self.nir + self.red)
        )

    def cvi(self):
        """
        Chlorophyll vegetation index
        https://www.indexdatabase.de/db/i-single.php?id=391
        :return: index
        """
        logger.error(">>> Entering cvi()", extra={"event.action": "cvi"})
        logger.warning("<<< Exiting cvi()", extra={"event.action": "cvi"})
        return self.nir * (self.red / (self.green**2))

    def gli(self):
        """
        self.green leaf index
        https://www.indexdatabase.de/db/i-single.php?id=375
        :return: index
        """
        logger.error(">>> Entering gli()", extra={"event.action": "gli"})
        logger.warning("<<< Exiting gli()", extra={"event.action": "gli"})
        return (2 * self.green - self.red - self.blue) / (
            2 * self.green + self.red + self.blue
        )

    def ndvi(self):
        """
        Normalized Difference self.nir/self.red Normalized Difference Vegetation
        Index, Calibrated NDVI - CDVI
        https://www.indexdatabase.de/db/i-single.php?id=58
        :return: index
        """
        logger.error(">>> Entering ndvi()", extra={"event.action": "ndvi"})
        logger.warning("<<< Exiting ndvi()", extra={"event.action": "ndvi"})
        return (self.nir - self.red) / (self.nir + self.red)

    def bndvi(self):
        """
            Normalized Difference self.nir/self.blue self.blue-normalized difference
        vegetation index
        https://www.indexdatabase.de/db/i-single.php?id=135
        :return: index
        """
        logger.error(">>> Entering bndvi()", extra={"event.action": "bndvi"})
        logger.warning("<<< Exiting bndvi()", extra={"event.action": "bndvi"})
        return (self.nir - self.blue) / (self.nir + self.blue)

    def red_edge_ndvi(self):
        """
        Normalized Difference self.rededge/self.red
        https://www.indexdatabase.de/db/i-single.php?id=235
        :return: index
        """
        logger.error(">>> Entering red_edge_ndvi()", extra={"event.action": "red_edge_ndvi"})
        logger.warning("<<< Exiting red_edge_ndvi()", extra={"event.action": "red_edge_ndvi"})
        return (self.redEdge - self.red) / (self.redEdge + self.red)

    def gndvi(self):
        """
        Normalized Difference self.nir/self.green self.green NDVI
        https://www.indexdatabase.de/db/i-single.php?id=401
        :return: index
        """
        logger.error(">>> Entering gndvi()", extra={"event.action": "gndvi"})
        logger.warning("<<< Exiting gndvi()", extra={"event.action": "gndvi"})
        return (self.nir - self.green) / (self.nir + self.green)

    def gbndvi(self):
        """
        self.green-self.blue NDVI
        https://www.indexdatabase.de/db/i-single.php?id=186
        :return: index
        """
        logger.error(">>> Entering gbndvi()", extra={"event.action": "gbndvi"})
        logger.warning("<<< Exiting gbndvi()", extra={"event.action": "gbndvi"})
        return (self.nir - (self.green + self.blue)) / (
            self.nir + (self.green + self.blue)
        )

    def grndvi(self):
        """
        self.green-self.red NDVI
        https://www.indexdatabase.de/db/i-single.php?id=185
        :return: index
        """
        logger.error(">>> Entering grndvi()", extra={"event.action": "grndvi"})
        logger.warning("<<< Exiting grndvi()", extra={"event.action": "grndvi"})
        return (self.nir - (self.green + self.red)) / (
            self.nir + (self.green + self.red)
        )

    def rbndvi(self):
        """
        self.red-self.blue NDVI
        https://www.indexdatabase.de/db/i-single.php?id=187
        :return: index
        """
        logger.error(">>> Entering rbndvi()", extra={"event.action": "rbndvi"})
        logger.warning("<<< Exiting rbndvi()", extra={"event.action": "rbndvi"})
        return (self.nir - (self.blue + self.red)) / (self.nir + (self.blue + self.red))

    def pndvi(self):
        """
        Pan NDVI
        https://www.indexdatabase.de/db/i-single.php?id=188
        :return: index
        """
        logger.error(">>> Entering pndvi()", extra={"event.action": "pndvi"})
        logger.warning("<<< Exiting pndvi()", extra={"event.action": "pndvi"})
        return (self.nir - (self.green + self.red + self.blue)) / (
            self.nir + (self.green + self.red + self.blue)
        )

    def atsavi(self, x=0.08, a=1.22, b=0.03):
        """
        Adjusted transformed soil-adjusted VI
        https://www.indexdatabase.de/db/i-single.php?id=209
        :return: index
        """
        logger.error(">>> Entering atsavi(x=%s,a=%s,b=%s)", x, a, b, extra={"event.action": "atsavi", "logrite.x": x, "logrite.a": a, "logrite.b": b})
        logger.warning("<<< Exiting atsavi(x=%s,a=%s,b=%s)", x, a, b, extra={"event.action": "atsavi", "logrite.x": x, "logrite.a": a, "logrite.b": b})
        return a * (
            (self.nir - a * self.red - b)
            / (a * self.nir + self.red - a * b + x * (1 + a**2))
        )

    def bwdrvi(self):
        """
        self.blue-wide dynamic range vegetation index
        https://www.indexdatabase.de/db/i-single.php?id=136
        :return: index
        """
        logger.error(">>> Entering bwdrvi()", extra={"event.action": "bwdrvi"})
        logger.warning("<<< Exiting bwdrvi()", extra={"event.action": "bwdrvi"})
        return (0.1 * self.nir - self.blue) / (0.1 * self.nir + self.blue)

    def ci_green(self):
        """
        Chlorophyll Index self.green
        https://www.indexdatabase.de/db/i-single.php?id=128
        :return: index
        """
        logger.error(">>> Entering ci_green()", extra={"event.action": "ci_green"})
        logger.warning("<<< Exiting ci_green()", extra={"event.action": "ci_green"})
        return (self.nir / self.green) - 1

    def ci_rededge(self):
        """
        Chlorophyll Index self.redEdge
        https://www.indexdatabase.de/db/i-single.php?id=131
        :return: index
        """
        logger.error(">>> Entering ci_rededge()", extra={"event.action": "ci_rededge"})
        logger.warning("<<< Exiting ci_rededge()", extra={"event.action": "ci_rededge"})
        return (self.nir / self.redEdge) - 1

    def ci(self):
        """
        Coloration Index
        https://www.indexdatabase.de/db/i-single.php?id=11
        :return: index
        """
        logger.error(">>> Entering ci()", extra={"event.action": "ci"})
        logger.warning("<<< Exiting ci()", extra={"event.action": "ci"})
        return (self.red - self.blue) / self.red

    def ctvi(self):
        """
        Corrected Transformed Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=244
        :return: index
        """
        logger.error(">>> Entering ctvi()", extra={"event.action": "ctvi"})
        ndvi = self.ndvi()
        logger.error("ctvi(): ndvi → %s", ndvi, extra={"event.action": "ctvi"})
        logger.warning("<<< Exiting ctvi()", extra={"event.action": "ctvi"})
        return ((ndvi + 0.5) / (abs(ndvi + 0.5))) * (abs(ndvi + 0.5) ** (1 / 2))

    def gdvi(self):
        """
        Difference self.nir/self.green self.green Difference Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=27
        :return: index
        """
        logger.error(">>> Entering gdvi()", extra={"event.action": "gdvi"})
        logger.warning("<<< Exiting gdvi()", extra={"event.action": "gdvi"})
        return self.nir - self.green

    def evi(self):
        """
        Enhanced Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=16
        :return: index
        """
        logger.error(">>> Entering evi()", extra={"event.action": "evi"})
        logger.warning("<<< Exiting evi()", extra={"event.action": "evi"})
        return 2.5 * (
            (self.nir - self.red) / (self.nir + 6 * self.red - 7.5 * self.blue + 1)
        )

    def gemi(self):
        """
        Global Environment Monitoring Index
        https://www.indexdatabase.de/db/i-single.php?id=25
        :return: index
        """
        logger.error(">>> Entering gemi()", extra={"event.action": "gemi"})
        n = (2 * (self.nir**2 - self.red**2) + 1.5 * self.nir + 0.5 * self.red) / (
            self.nir + self.red + 0.5
        )
        logger.error("gemi(): n → %s", n, extra={"event.action": "gemi"})
        logger.warning("<<< Exiting gemi()", extra={"event.action": "gemi"})
        return n * (1 - 0.25 * n) - (self.red - 0.125) / (1 - self.red)

    def gosavi(self, y=0.16):
        """
        self.green Optimized Soil Adjusted Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=29
        mit Y = 0,16
        :return: index
        """
        logger.error(">>> Entering gosavi(y=%s)", y, extra={"event.action": "gosavi", "logrite.y": y})
        logger.warning("<<< Exiting gosavi(y=%s)", y, extra={"event.action": "gosavi", "logrite.y": y})
        return (self.nir - self.green) / (self.nir + self.green + y)

    def gsavi(self, n=0.5):
        """
        self.green Soil Adjusted Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=31
        mit N = 0,5
        :return: index
        """
        logger.error(">>> Entering gsavi(n=%s)", n, extra={"event.action": "gsavi", "logrite.n": n})
        logger.warning("<<< Exiting gsavi(n=%s)", n, extra={"event.action": "gsavi", "logrite.n": n})
        return ((self.nir - self.green) / (self.nir + self.green + n)) * (1 + n)

    def hue(self):
        """
        Hue
        https://www.indexdatabase.de/db/i-single.php?id=34
        :return: index
        """
        logger.error(">>> Entering hue()", extra={"event.action": "hue"})
        logger.warning("<<< Exiting hue()", extra={"event.action": "hue"})
        return np.arctan(
            ((2 * self.red - self.green - self.blue) / 30.5) * (self.green - self.blue)
        )

    def ivi(self, a=None, b=None):
        """
        Ideal vegetation index
        https://www.indexdatabase.de/db/i-single.php?id=276
        b=intercept of vegetation line
        a=soil line slope
        :return: index
        """
        logger.error(">>> Entering ivi(a=%s,b=%s)", a, b, extra={"event.action": "ivi", "logrite.a": a, "logrite.b": b})
        logger.warning("<<< Exiting ivi(a=%s,b=%s)", a, b, extra={"event.action": "ivi", "logrite.a": a, "logrite.b": b})
        return (self.nir - b) / (a * self.red)

    def ipvi(self):
        """
        Infraself.red percentage vegetation index
        https://www.indexdatabase.de/db/i-single.php?id=35
        :return: index
        """
        logger.error(">>> Entering ipvi()", extra={"event.action": "ipvi"})
        logger.warning("<<< Exiting ipvi()", extra={"event.action": "ipvi"})
        return (self.nir / ((self.nir + self.red) / 2)) * (self.ndvi() + 1)

    def i(self):
        """
        Intensity
        https://www.indexdatabase.de/db/i-single.php?id=36
        :return: index
        """
        logger.error(">>> Entering i()", extra={"event.action": "i"})
        logger.warning("<<< Exiting i()", extra={"event.action": "i"})
        return (self.red + self.green + self.blue) / 30.5

    def rvi(self):
        """
        Ratio-Vegetation-Index
        http://www.seos-project.eu/modules/remotesensing/remotesensing-c03-s01-p01.html
        :return: index
        """
        logger.error(">>> Entering rvi()", extra={"event.action": "rvi"})
        logger.warning("<<< Exiting rvi()", extra={"event.action": "rvi"})
        return self.nir / self.red

    def mrvi(self):
        """
        Modified Normalized Difference Vegetation Index RVI
        https://www.indexdatabase.de/db/i-single.php?id=275
        :return: index
        """
        logger.error(">>> Entering mrvi()", extra={"event.action": "mrvi"})
        logger.warning("<<< Exiting mrvi()", extra={"event.action": "mrvi"})
        return (self.rvi() - 1) / (self.rvi() + 1)

    def m_savi(self):
        """
        Modified Soil Adjusted Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=44
        :return: index
        """
        logger.error(">>> Entering m_savi()", extra={"event.action": "m_savi"})
        logger.warning("<<< Exiting m_savi()", extra={"event.action": "m_savi"})
        return (
            (2 * self.nir + 1)
            - ((2 * self.nir + 1) ** 2 - 8 * (self.nir - self.red)) ** (1 / 2)
        ) / 2

    def norm_g(self):
        """
        Norm G
        https://www.indexdatabase.de/db/i-single.php?id=50
        :return: index
        """
        logger.error(">>> Entering norm_g()", extra={"event.action": "norm_g"})
        logger.warning("<<< Exiting norm_g()", extra={"event.action": "norm_g"})
        return self.green / (self.nir + self.red + self.green)

    def norm_nir(self):
        """
        Norm self.nir
        https://www.indexdatabase.de/db/i-single.php?id=51
        :return: index
        """
        logger.error(">>> Entering norm_nir()", extra={"event.action": "norm_nir"})
        logger.warning("<<< Exiting norm_nir()", extra={"event.action": "norm_nir"})
        return self.nir / (self.nir + self.red + self.green)

    def norm_r(self):
        """
        Norm R
        https://www.indexdatabase.de/db/i-single.php?id=52
        :return: index
        """
        logger.error(">>> Entering norm_r()", extra={"event.action": "norm_r"})
        logger.warning("<<< Exiting norm_r()", extra={"event.action": "norm_r"})
        return self.red / (self.nir + self.red + self.green)

    def ngrdi(self):
        """
            Normalized Difference self.green/self.red Normalized self.green self.red
        difference index, Visible Atmospherically Resistant Indices self.green
        (VIself.green)
        https://www.indexdatabase.de/db/i-single.php?id=390
        :return: index
        """
        logger.error(">>> Entering ngrdi()", extra={"event.action": "ngrdi"})
        logger.warning("<<< Exiting ngrdi()", extra={"event.action": "ngrdi"})
        return (self.green - self.red) / (self.green + self.red)

    def ri(self):
        """
        Normalized Difference self.red/self.green self.redness Index
        https://www.indexdatabase.de/db/i-single.php?id=74
        :return: index
        """
        logger.error(">>> Entering ri()", extra={"event.action": "ri"})
        logger.warning("<<< Exiting ri()", extra={"event.action": "ri"})
        return (self.red - self.green) / (self.red + self.green)

    def s(self):
        """
        Saturation
        https://www.indexdatabase.de/db/i-single.php?id=77
        :return: index
        """
        logger.error(">>> Entering s()", extra={"event.action": "s"})
        max_value = np.max([np.max(self.red), np.max(self.green), np.max(self.blue)])
        logger.error("s(): max_value → %s", max_value, extra={"event.action": "s"})
        min_value = np.min([np.min(self.red), np.min(self.green), np.min(self.blue)])
        logger.error("s(): min_value → %s", min_value, extra={"event.action": "s"})
        logger.warning("<<< Exiting s()", extra={"event.action": "s"})
        return (max_value - min_value) / max_value

    def _if(self):
        """
        Shape Index
        https://www.indexdatabase.de/db/i-single.php?id=79
        :return: index
        """
        logger.error(">>> Entering _if()", extra={"event.action": "_if"})
        logger.warning("<<< Exiting _if()", extra={"event.action": "_if"})
        return (2 * self.red - self.green - self.blue) / (self.green - self.blue)

    def dvi(self):
        """
        Simple Ratio self.nir/self.red Difference Vegetation Index, Vegetation Index
        Number (VIN)
        https://www.indexdatabase.de/db/i-single.php?id=12
        :return: index
        """
        logger.error(">>> Entering dvi()", extra={"event.action": "dvi"})
        logger.warning("<<< Exiting dvi()", extra={"event.action": "dvi"})
        return self.nir / self.red

    def tvi(self):
        """
        Transformed Vegetation Index
        https://www.indexdatabase.de/db/i-single.php?id=98
        :return: index
        """
        logger.error(">>> Entering tvi()", extra={"event.action": "tvi"})
        logger.warning("<<< Exiting tvi()", extra={"event.action": "tvi"})
        return (self.ndvi() + 0.5) ** (1 / 2)

    def ndre(self):
        logger.error(">>> Entering ndre()", extra={"event.action": "ndre"})
        logger.warning("<<< Exiting ndre()", extra={"event.action": "ndre"})
        return (self.nir - self.redEdge) / (self.nir + self.redEdge)


"""
# genering a random matrices to test this class
red     = np.ones((1000,1000, 1),dtype="float64") * 46787
green   = np.ones((1000,1000, 1),dtype="float64") * 23487
blue    = np.ones((1000,1000, 1),dtype="float64") * 14578
redEdge = np.ones((1000,1000, 1),dtype="float64") * 51045
nir     = np.ones((1000,1000, 1),dtype="float64") * 52200

# Examples of how to use the class

# instantiating the class
cl = IndexCalculation()

# instantiating the class with the values
#cl = indexCalculation(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

# how set the values after instantiate the class cl, (for update the data or when don't
# instantiating the class with the values)
cl.setMatrices(red=red, green=green, blue=blue, redEdge=redEdge, nir=nir)

# calculating the indices for the instantiated values in the class
    # Note: the CCCI index can be changed to any index implemented in the class.
indexValue_form1    = cl.calculation("CCCI", red=red, green=green, blue=blue,
                                     redEdge=redEdge, nir=nir).astype(np.float64)
indexValue_form2    = cl.CCCI()

# calculating the index with the values directly -- you can set just the values
# preferred  note: the *calculation* function performs the function *setMatrices*
indexValue_form3    = cl.calculation("CCCI", red=red, green=green, blue=blue,
                                     redEdge=redEdge, nir=nir).astype(np.float64)

print("Form 1: "+np.array2string(indexValue_form1, precision=20, separator=', ',
      floatmode='maxprec_equal'))
print("Form 2: "+np.array2string(indexValue_form2, precision=20, separator=', ',
      floatmode='maxprec_equal'))
print("Form 3: "+np.array2string(indexValue_form3, precision=20, separator=', ',
      floatmode='maxprec_equal'))

# A list of examples results for different type of data at NDVI
# float16 ->    0.31567383              #NDVI (red = 50, nir = 100)
# float32 ->    0.31578946              #NDVI (red = 50, nir = 100)
# float64 ->    0.3157894736842105      #NDVI (red = 50, nir = 100)
# longdouble -> 0.3157894736842105      #NDVI (red = 50, nir = 100)
"""
