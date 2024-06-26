import json

from stockdatawrapper.endpoints import Endpoint
from datetime import datetime
import pkg_resources


class RequestValidator:
    def __init__(self) -> None:
        self.endpoint_data = {}
        self.endpoint_data = json.loads(pkg_resources.resource_string(__name__, 'validation.json'))
        if self.endpoint_data == {}:
            raise Exception(f"There is an issue with endpoint data json, please check")

    def validate(self, endpoint=Endpoint) -> bool:
        # Check if the endpoint type is valid
        if endpoint.type not in self.endpoint_data.keys():
            raise Exception(f"Endpoint {endpoint.type} does not match any listef in the validation.json")
        
        required_arguments = self.endpoint_data[endpoint.type]['required']
        optional_arguments = self.endpoint_data[endpoint.type]['optional']
        all_arguments = self.endpoint_data[endpoint.type]['required'].copy()
        all_arguments.update(optional_arguments)
        # Check if endpoint instance has all required arguments 
        for required_argument in required_arguments.keys():
            if required_argument not in endpoint.parameters.keys():
                raise Exception(f"A required argument {required_argument} has not been passed")
        
        # Check if the passed arguments are of the correct types and no rogue arguments
        # were passed
        for argument, value in endpoint.parameters.items():
            if (argument not in required_arguments.keys()) and (argument not in optional_arguments.keys()):
                raise Exception(f"You are trying to pass a rogue argument {argument} to endpoint for {endpoint.type}. It doesn't work that way.")
            
            
            argument_params = all_arguments[argument]
            acceptable_type = argument_params['type']
            acceptable_type = acceptable_type.split('|')
            for i, s in enumerate(acceptable_type):
                acceptable_type[i] = eval(s)
            if type(value) not in acceptable_type:
                raise Exception(f"Looks like you specified {type(value)} type for {argument} argument. This argument is set up to take {acceptable_type}")
            
            # Check for option adherance 
            if 'options' in argument_params.keys():
                if value not in argument_params['options']:
                    raise Exception(f"{value} is not an acceptable option for {argument}. Choose from {argument_params['options']}")
                
            # Check for timestamp formatting
            if 'timestamp_formats' in argument_params.keys():
                acceptable_date_formats = argument_params['timestamp_formats']
                date_checks = []
                for format in acceptable_date_formats:
                    try:
                        datetime.strptime(value, format)
                        date_checks.append(True)
                    except:
                        date_checks.append(False)
                if True not in date_checks:
                    raise Exception(f"Your date {value} does not fit any of the available time formats {acceptable_date_formats}")
                
            # Check for ranged arguments
            if 'min' in argument_params.keys():
                if value < argument_params['min']:
                    raise Exception(f"Your specified {value} for {argument}, that is less than possible minimum of {argument_params['min']}")
            if 'max' in argument_params.keys():
                if value > argument_params['max']:
                    raise Exception(f"Your specified {value} for {argument}, that is greater than possible maximum of {argument_params['max']}")

        
        endpoint.is_valid=True

        # Constructing url
        url = self.endpoint_data[endpoint.type]['url']
        for argument, value in endpoint.parameters.items():
            if type(value) == list:
                url += f"{argument}={','.join(value)}&"
            elif argument == 'uuid':
                url += f"{value}"
            else:
                url += f"{argument}={value}&"
        url = url[:-1]
        print(url)
        endpoint.url = url
