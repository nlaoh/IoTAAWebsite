import os

# Define the target directory
target_directory = "html_versions"

# Define the starting directory path
starting_directory = r'D:\GIT_REPOS\personalprojects\IoTAAWebsite\learn_page'

initial_html_content = """
<!-- External Stylesheet (DO NOT REMOVE) -->
<link rel="stylesheet" type="text/css" href="https://cdn.ymaws.com/iot.site-ym.com/styles/custompages.css" />

<!-- Internal Styles (Page Styles) -->
<style>
/* Hero */

/* Boxes */
#resources2-boxes1 .section-header, #resources2-boxes2 .section-header { text-align: center; margin-bottom: 10px; }
#resources2-boxes1 .cb-box, 
#resources2-boxes2 .cb-box { margin: 30px 0 0; }

/*** Media Queries ***/
@media (max-width: 767px) {

}

/* Dropdown box */
.data {
    background: #f7f7f7;
    padding: 20px;
    margin: 30px 8px 35px;
    position: relative;
}
.dataContent h2 {
    margin-top: 0;
}
.close {
    position: absolute;
    right: 16px;
    z-index: 100;
    font-size: 12px;
    text-decoration: underline;
}
.close:hover {
    color: #222;
    text-decoration: underline;
}
</style>

<!-- Top Hero Starts -->
<div class="sp-hero-out" id="resources2-hero"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/banner2.jpeg" alt="/" class="img-responsive" />
    <div class="container">
        <div class="sp-hero-content">
            <h1>RESOURCES</h1>
        </div>
    </div>
</div>

<!-- Featured Info Starts -->
<div class="sp-content-out bg-grey text-center" id="resources2-featured">
    <div class="container">
        <div class="row">
            <div class="col-sm-12">
                <p>IOTAA produces a range of publications and resources for its members and wider IoT, business and education community including research reports and white papers.</p>
            </div>
        </div>
    </div>
</div>

<!-- Boxes Starts -->
<div class="sp-content-out" id="resources2-boxes1">
    <div class="container">
        <!-- Row 1 Boxes -->
        <div class="row">
            <!-- Box 1 -->
            <div class="col-md-6 cb-left">
                <div class="cb-box row">
                    <!-- Image -->
                    <div class="col-xs-6 cb-img"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/banner.jpeg" alt="/" /> </div>
                    <!-- Info -->
                    <div class="col-xs-6 cb-text">
                        <h5>Case Studies</h5>
                        <p>A case study is an in-depth, detailed examination of a particular case (or cases) within a real-world context. The content here is provided by our membership and related organizations.</p>
                        <a class="formbutton dataBTN" data-target="#data1">Access</a> 
                    </div>
                </div>
            </div>
            <!-- Box 2 -->
            <div class="col-md-6 cb-right">
                <div class="cb-box row">
                    <!-- Image -->
                    <div class="col-xs-6 cb-img"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/banner1.jpeg" alt="/" /> </div>
                    <!-- Info -->
                    <div class="col-xs-6 cb-text">
                        <h5>Advocacy</h5>
                        <p>Our organization engages in many government submissions and policy regulations and standards for IoT. The content reflects some of the contributions made.</p>
                        <a class="formbutton dataBTN" data-target="#data2">Access</a> 
                    </div>
                </div>
            </div>
        </div>
        <!-- Row 1 Data -->
        <div class="row">
            <div id="data1" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Case Studies</h3>
                    <p>
                        Frank is a thought leader in the adoption of Internet of Things (IoT), 
                        and the founding CEO of IoTAA. 
                        He is a Partner Manager for the Reliable Affordable Clean Energy for 
                        2030 Cooperative Research Centre (RACE for 2030), an industry-led
                        an initiative that fosters innovation across the energy supply chain to deliver 
                        increased value for consumers. 
                        Frank is also on the board of the NSW Smart Sensing Network, which brings 
                        together smart sensing expertise in academia,
                        industry and government to deliver economic and social benefits for NSW.
                    </p>
                </div>
            </div>
            <div id="data2" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Advocacy</h3>
                    <ul>
                        <a href="/resource/resmgr/iotaa_response_to_ai_regulat.pdf" target="_blank">26th July 2023 - IoTAA response to AI regulation</a>
                    </ul>
                </div>
            </div>
        </div>
        <!-- Row 2 Boxes -->
        <div class="row">
            <!-- Box 3 -->
            <div class="col-md-6 cb-left">
                <div class="cb-box row">
                    <!-- Image -->
                    <div class="col-xs-6 cb-img"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/links.jpeg" alt="/" /> </div>
                    <!-- Info -->
                    <div class="col-xs-6 cb-text">
                        <h5>Useful Links</h5>
                        <a class="formbutton dataBTN" data-target="#data3">Access</a> 
                    </div>
                </div>
            </div>
            <!-- Box 4 -->
            <div class="col-md-6 cb-right">
                <div class="cb-box row">
                    <!-- Image -->
                    <div class="col-xs-6 cb-img"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/thought-leadership.jpg" alt="/" /> </div>
                    <!-- Info -->
                    <div class="col-xs-6 cb-text">
                        <h5>Thought Leadership</h5>
                        <p>Our association leads and has considerable expertise in Internet of Things. Over the past few years, the IoTAA has contributed to thought leadership in various ways.</p>
                        <a class="formbutton dataBTN" data-target="#data4">Access</a> 
                    </div>
                </div>
            </div>
        </div>
        <!-- Row 2 Data -->
        <div class="row">
            <div id="data3" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Useful Links</h3>
                    <a href="https://ia.acs.org.au" target="_blank">Australian Computer Society Information Age Newsletter</a>
                    <br>
                    <a href="https://commsalliance.com.au" target="_blank">Communications Alliance</a>
                    <br>
                    <a href="https://iiconsortium.org" target="_blank">Industrial Internet Consortium</a>
                    <br>
                    <a href="https://platformi-40.de" target="_blank">Industrie 4 in Germany</a>
                    <br>
                    <a href="https://iothub.com.au" target="_blank">IOT Hub – connecting you to the internet of things</a>
                    <br>
                    <a href="https://itu.int/eu" target="_blank">ITU’s Smart Sustainable Cities</a>
                    <br>
                    <a href="https://iot-analytics.com/" target="_blank">IoT Analytics</a>
                    <br>
                </div>
            </div>
            <div id="data4" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Thought Leadership</h3>
                    <p>
                        Frank is a thought leader in the adoption of Internet of Things (IoT), 
                        and the founding CEO of IoTAA. 
                        He is a Partner Manager for the Reliable Affordable Clean Energy for 
                        2030 Cooperative Research Centre (RACE for 2030), an industry-led
                        an initiative that fosters innovation across the energy supply chain to deliver 
                        increased value for consumers. 
                        Frank is also on the board of the NSW Smart Sensing Network, which brings 
                        together smart sensing expertise in academia,
                        industry and government to deliver economic and social benefits for NSW.
                    </p>
                </div>
            </div>
        </div>
        <!-- Row 3 Boxes -->
        <div class="row">
            <!-- Box 7 -->
            <div class="col-md-6 cb-left">
                <div class="cb-box row">
                    <!-- Image -->
                    <div class="col-xs-6 cb-img"> <img src="https://staging-iot.site-ym.com/resource/resmgr/learn-page_images/guidelines.jpeg" alt="/" /> </div>
                    <!-- Info -->
                    <div class="col-xs-6 cb-text">
                        <h5>Guidelines &amp; Codes of Practice</h5>
                        <p>This comprises of whitepapers, greenpapers, manuals, and other position paper generated by the IoTAA membership.</p>
                        <a class="formbutton dataBTN" data-target="#data5">Access</a> </div>
                </div>
            </div>
        </div>
        <!-- Row 3 Data -->
        <div class="row">
            <div id="data5" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Guidelines &amp; Codes of Practice</h3>
                    <p>
                        Frank is a thought leader in the adoption of Internet of Things (IoT), 
                        and the founding CEO of IoTAA. 
                        He is a Partner Manager for the Reliable Affordable Clean Energy for 
                        2030 Cooperative Research Centre (RACE for 2030), an industry-led
                        an initiative that fosters innovation across the energy supply chain to deliver 
                        increased value for consumers. 
                        Frank is also on the board of the NSW Smart Sensing Network, which brings 
                        together smart sensing expertise in academia,
                        industry and government to deliver economic and social benefits for NSW.
                    </p>
                </div>
            </div>
            <!-- This is commented out as there is no sixth box -->
            <!-- <div id="data6" class="data" style="display: none;"> 
                <div class="container" style="width: 100%">
                    <a class="close" style="position: relative;">Close</a>
                    <h3>Thought Leadership</h3>
                    <p>
                        Frank is a thought leader in the adoption of Internet of Things (IoT), 
                        and the founding CEO of IoTAA. 
                        He is a Partner Manager for the Reliable Affordable Clean Energy for 
                        2030 Cooperative Research Centre (RACE for 2030), an industry-led
                        an initiative that fosters innovation across the energy supply chain to deliver 
                        increased value for consumers. 
                        Frank is also on the board of the NSW Smart Sensing Network, which brings 
                        together smart sensing expertise in academia,
                        industry and government to deliver economic and social benefits for NSW.
                    </p>
                </div>
            </div> -->
        </div>
    </div>
</div>

<!-- Script for Dropdown Bios -->
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

<script>
    $(document).ready(function(){	
      //Hide Bios//
      var bioInfo = $('.data').hide();
      //Click and bio Animation//
      $('.dataBTN').click(function(){
    	var target = $(this).data("target");
    	//Hide Open Bios When cliking Other Bio
    	$(".data").slideUp();
    	//Open Target Bio// 
    	$(target).slideDown();	
    	return false ;
      });
      //close button Inside the bio
      $('.close').click(function(){
        var myTarget = $(this).closest('.data'); // Find the closest parent div with class "data"
        myTarget.slideUp();
        return false;
    	});
      //Close Bio by cliking outside  	
      var $win = $(window); // or $box parent container
      var $box = $(".box");
      $win.on("click.Bst", function(event){		
    	if ( $(".data").has(event.target).length == 0 && !$(".data").is(event.target) //checks if the $box itself was clicked
    ){
    	$(".data").slideUp();
    	}
      });		  
    });
</script>
"""

# Walk through all directories starting from the specified path
for root, dirs, files in os.walk(starting_directory):
    if target_directory in dirs:
        # The target directory already exists in this directory
        target_dir = os.path.join(root, target_directory)
        html_file_path = os.path.join(target_dir, 'v1_default.html')

        # Extract the directory name from the path
        directory_name = os.path.basename(root)

        # Replace underscores with spaces in the directory name
        directory_name = directory_name.replace('_', ' ')

        # Create a copy of the initial HTML content
        html_content = initial_html_content

        # Replace [Placeholder] with the directory name in the HTML content
        html_content = html_content.replace('[Placeholder]', directory_name)

        with open(html_file_path, 'w') as html_file:
            html_file.write(html_content)

print("v1_default.html files added to existing directories in html_versions")
