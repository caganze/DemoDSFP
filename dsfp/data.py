import astropy
import astroquery
from astroquery.sdss import SDSS #do queries on sdss server
from astroquery.simbad import Simbad

def get_photometry(N=10000):
    
    """ Get photometry from the SDSS Database 
    Parameters
    ----------
    N: int 
       number of objects
    Returns
    -------
    data: astropy.table
    """
    query=""" SELECT TOP 10000 
    p.psfMag_r, p.fiberMag_r, p.fiber2Mag_r, p.petroMag_r, 
    p.deVMag_r, p.expMag_r, p.modelMag_r, p.cModelMag_r, 
    s.class
    FROM PhotoObjAll AS p JOIN specObjAll s ON s.bestobjid = p.objid
    WHERE p.mode = 1 AND s.sciencePrimary = 1 AND p.clean = 1 AND s.class != 'QSO'
    ORDER BY p.objid ASC """
    data=SDSS.query_sql(query.format(N=N))
    return data