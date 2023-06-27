import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx']

    def parse(self, response):
        # Extract the available options for the first dropdown
        state_options = response.xpath('//select[@id="ContentPlaceHolder1_DropDownState"]/option')[1:]
        
        # Iterate over the state options and make requests for subsequent dropdowns
        for option in state_options:
            state_value = option.xpath('@value').get()
            state_name = option.xpath('text()').get()

            # Make a request for the second dropdown using the selected state value
            yield scrapy.FormRequest.from_response(
                response,
                formdata={'state_dropdown_name': state_value},
                callback=self.parse_districts,
                meta={'state_name': state_name}
            )
        