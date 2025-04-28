import boto3

def get_security_groups(ec2_client):
    try:
        #Try to retrieve all security groups
        response = ec2_client.describe_security_groups()
        
        #Check if any security groups are returned
        #If so, print the group IDs of the security groups
        if response['SecurityGroups']:
            
            #Iterate through the security groups and print their IDs
            for sg in response['SecurityGroups']:
                print(f"{sg['GroupId']}")
                
    except Exception as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    #Create an EC2 client
    ec2_client = boto3.client('ec2')
    
    #Call the function to get security groups
    get_security_groups(ec2_client)