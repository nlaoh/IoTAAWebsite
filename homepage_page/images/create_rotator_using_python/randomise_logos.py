import random

html_code = '''
            <div class="logo">
                <a href="https://accan.org.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/accan.jpg" alt="accan.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.accc.gov.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/accc.jpg" alt="accc.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.acma.gov.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/acma.jpg" alt="acma.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.adasasystems.com/en/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/adasa.jpg" alt="adasa.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://aiia.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/aiia.jpg" alt="aiia.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://amta.org.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/amta.jpg" alt="amta.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.blueiot.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/blue_iot.jpg" alt="blue_iot.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.bosch.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/bosch.jpg" alt="bosch.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.commsalliance.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/communications_alliance.jpg" alt="communications_alliance.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://cradlepoint.com/en-au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/cradlepoint.jpg" alt="cradlepoint.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.csiro.au/en/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/csiro.jpg" alt="csiro.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.deakin.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/deakin.jpg" alt="deakin.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.deloitte.com/au/en.html"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/deloitte.jpg" alt="deloitte.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://fleetspace.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/fleet.jpg" alt="fleet.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.ghd.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/ghd.jpg" alt="ghd.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://holmes.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/homes.jpg" alt="homes.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.ibm.com/au-en"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/ibm.jpg" alt="ibm.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.inauro.io/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/inauro.jpg" alt="inauro.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.inmarsat.com/en/index.html"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/inmarsat.jpg" alt="inmarsat.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.internetsociety.org/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/internet_australia.jpg" alt="internet_australia.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://iotskills.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/iot_skills.jpg" alt="iot_skills.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://kpmg.com/au/en/home.html"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/kpmg.jpg" alt="kpmg.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.lenovo.com/au/en/pc/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/lenovo.jpg" alt="lenovo.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.mq.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/macquarie.jpg" alt="macquarie.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.meshed.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/meshed.jpg" alt="meshed.jpg" /></a>
            </div>
            <div class="logo">
                <a href="#"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/miot.jpg" alt="miot.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://myriota.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/myriota.jpg" alt="myriota.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.nbnco.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/nbn.png" alt="nbn.png" /></a>
            </div>
            <div class="logo">
                <a href="https://www.nec.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/nec.jpg" alt="nec.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.optus.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/optus.jpg" alt="optus.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://reekoh.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/reekoh.jpg" alt="reekoh.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.rmit.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/rmit.jpg" alt="rmit.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.rockwellautomation.com/en-us.html"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/rockwell.jpg" alt="rockwell.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://southeastwater.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/sew.jpg" alt="sew.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://simocowirelesssolutions.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/simoco.jpg" alt="simoco.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.suez.com/en/australia-new-zealand"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/suez.jpg" alt="suez.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.swinburne.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/swinburne.jpg" alt="swinburne.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.sydneywater.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/sydney_water.jpg" alt="sydney_water.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.taoglas.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/taoglas.jpg" alt="taoglas.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.tatacommunications.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/tata.jpg" alt="tata.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.telit.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/telit.jpg" alt="telit.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.telstra.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/telstra.jpg" alt="telstra.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://thinxtra.com/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/thinxtra.jpg" alt="thinxtra.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.tpgtelecom.com.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/tpg.jpg" alt="tpg.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.urban.org/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/urban.jpg" alt="urban.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.uts.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/uts.jpg" alt="uts.jpg" /></a>
            </div>
            <div class="logo">
                <a href="https://www.uow.edu.au/"> <img src="https://cdn.ymaws.com/staging-iot.site-ym.com/resource/resmgr/logo_images/wollongong.jpg" alt="wollongong.jpg" /></a>
            </div>
'''

# Split the HTML code into individual <div> elements
div_elements = html_code.split('<div class="logo">')[1:]

# randomise
random.shuffle(div_elements)

# Process each <div> element (you can add your own logic here)
for div in div_elements:
    div = '            <div class="logo">' + div  # Add back the '<div class="logo">' tag
    # Perform operations on the individual <div> element
    print(div)  # Replace 'print' with your desired operation