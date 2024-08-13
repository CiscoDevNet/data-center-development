<h1 align="center">Using Python to Automate the Nexus Dashboard Fabric Controller (NDFC)</h1>
<p align="center">
<img src="https://github.com/user-attachments/assets/69a9e875-fef8-41ea-a24f-1f4a307aeed4" width="150">
</p>

## Overview 

Here you will find scripts to automate actions in NDFC. The code generated here was created by using [Postman](https://www.postman.com/downloads/) to convert the API calls to Python with the 'Code' tab. The code works against the *reservable* [vNexus Dashboard Controller sandbox](https://devnetsandbox.cisco.com/DevNet/catalog/vnexus-dashboard-fabric-controller_vnexus-dashboard-fabric-controller) from Cisco DevNet.

<br>

## The Python Scripts


> Note: These scripts store and use the Cookie in/from a file called **ndfc_token.txt**. We've added it to the .gitignore to prevent it being published to GitHub but this is still not a secure way to store and use this token in production and is only being utlilized for demo purposes.


1. [login_ndfc.py](./login_ndfc.py) - login using username and password. Verification is set to False to bypass the certificate error, so don't use in production.

The results will include the certificate warning (which you can ignore in this training) as well as the response code:

python3 login_ndfc.py 
/Users/alexstev/Data-Center/data-center-development/venv/lib/python3.11/site-packages/urllib3/connectionpool.py:1099: InsecureRequestWarning: Unverified HTTPS request is being made to host '10.10.20.60'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
Login Response Status Code: 200

<br>

**You *must* run this script first before running other scripts**


2. [get_switches_ndfc.py](./lget_switches_ndfc.py) - returns all switches in the inventory. Example output (truncated for brevity):


[{"switchRoleEnum":"EdgeRouter","vrf":"management","fabricTechnology":"External","deviceType":"External","fabricId":3,"name":null,"domainID":0,"wwn":null,"membership":null,"ports":0,"model":"N9K-C9300v","version":null,"upTime":0,"ipAddress":"10.10.20.180","mgmtAddress":null,"vendor":"Cisco","displayHdrs":null,"displayValues":null,"colDBId":0,"fid":0,"isLan":false,"is_smlic_enabled":false,"present":true,

<br>

3. [get_fabrics_ndfc.py](./lget_fabrics_ndfc.py) - returns all of the fabrics in the inventory. Example outut (truncated for brevity):


[{"id":2,"fabricId":"FABRIC-2","fabricName":"DevNet_Fabric","fabricType":"Switch_Fabric","fabricTypeFriendly":"Switch Fabric","fabricTechnology":"VXLANFabric","fabricTechnologyFriendly":"VXLAN EVPN","provisionMode":"DCNMTopDown","deviceType":"n9k","replicationMode":"Multicast","operStatus":"MINOR","asn":"65001","siteId":"65001","templateName":"Easy_Fabric","nvPairs":{"MSO_SITE_ID":"","PHANTOM_RP_LB_ID1":"","PHANTOM_RP_LB_ID2":"","PHANTOM_RP_LB_ID3":"","IBGP_PEER_TEMPLATE":"","PHANTOM_RP_LB_ID4":"",

<br>

4. [get_vrfs_ndfc.py](./get_vrfs_ndfc.py) - returns all VRFs in the designated fabric. If you're using the DevNet NDFC sandbox, the initial configuration of the DevNet _Fabric will not have any VRFs, so an empty list will be returned:

[]

<br>

5. [create_vrf_ndfc.py](./create_vrf_ndfc.py) - creates a VRF called "VRF_Python" in the DevNet _Fabric. The output will include:

```
The following VRF was created: {"VRF Id":51000,"VRF Name":"VRF_PYTHON"}
```

> You can also verifiy the VRF was created with the **get_vrfs_ndc.py** script above

<br>

6. [create_vrf_ndfc.py](./delete_vrf_ndfc.py) - deletes the VRF "VRF_Python" in the DevNet _Fabric. The output will include:

```
Successfully deleted VRF: VRF_PYTHON
```

> You can also verifiy the VRF was created with the **get_vrfs_ndc.py** script above

