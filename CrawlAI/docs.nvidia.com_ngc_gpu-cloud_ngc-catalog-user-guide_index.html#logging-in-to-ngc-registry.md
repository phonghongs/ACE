Submit Search
  * [NVIDIA Developer](https://developer.nvidia.com/)
  * [Blog](https://developer.nvidia.com/blog/)
  * [Forums](https://forums.developer.nvidia.com/)
  * [Join](https://docs.nvidia.com/login)


[ ![NVIDIA Documentation Home](https://docscontent.nvidia.com/bf/6f/f2d5da4743aebb3dff0e6a6129ec/nvidia-docshub-logo-2.svg) ](https://docs.nvidia.com/) Submit Search
  * [NVIDIA Developer](https://developer.nvidia.com/)
  * [Blog](https://developer.nvidia.com/blog/)
  * [Forums](https://forums.developer.nvidia.com/)
  * [Join](https://docs.nvidia.com/login)


Menu
[ ](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html)
User Guide
Submit Search
Submit Search
[NVIDIA Docs Hub](https://docs.nvidia.com/) [NVIDIA NGC](https://docs.nvidia.com/ngc/index.html) [User Guide](https://docs.nvidia.com/ngc/gpu-cloud/index.html) [NGC Catalog User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html)
[Download PDF](https://docs.nvidia.com/ngc/gpu-cloud/pdf/ngc-catalog-user-guide.pdf)
# [NGC Catalog User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html)
##  [NGC Catalog User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#abstract)
This user guide details how to navigate the NGC Catalog and step-by-step instructions on downloading and using content.
## [1. What is the NGC Catalog?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#what-is-ngc-catalog)
The NGC Catalog is a curated set of GPU-optimized software for AI, HPC and Visualization. 
The content provided by NVIDIA and third-party ISVs simplifies building, customizing, and integrating GPU-optimized software into workflows, accelerating the time to solutions for users. 
The NGC Catalog consists of containers, pre-trained models, Helm charts for Kubernetes deployments, and industry-specific AI toolkits with software development kits (SDKs). 
##  Containers 
The NGC Catalog hosts a broad range of containers, including deep learning frameworks, machine learning, HPC, and visualization applications that maximize the utilization of GPU environments. Containers package software applications, libraries, dependencies, and run-time compilers in a self-contained environment to easily deploy them across various computing environments. They enable software portability, and through a single command, users can pull, run and scale applications across the cloud, the data center, and the edge. 
##  [Models and Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#what-is-ngc-catalog__section_vsc_l2y_3mb)
The NGC Catalog offers pre-trained models for a wide range of common AI tasks optimized for NVIDIA Tensor Core GPUs. The pre-trained models can be used for inference or fine-tuned with transfer learning, saving data scientists and developers valuable time. 
Resources offer documentation, code samples, and many other assets such as Jupyter Notebooks, deployment pipelines, and step-by-step instructions and scripts for creating deep learning models, making it easy to get started with deep learning. 
##  [Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#what-is-ngc-catalog__section_arj_l2y_3mb)
Kubernetes is a container orchestrator that facilitates the deployment and management of containerized applications and microservices. A Helm chart is a package manager that allows DevOps to configure, deploy and update applications across Kubernetes environments more efficiently. The NGC Catalog provides Helm charts for deploying GPU-optimized applications and SDKs. 
##  [Software Development Kits](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#what-is-ngc-catalog__section_qmm_l2y_3mb)
SDKs deliver all the tooling users need to build and deploy AI applications across domains such as medical imaging, conversational AI, or video analytics. They include annotation tools for data labeling, pre-trained models for customization with transfer learning, and SDKs that enable deployment across the cloud, the data center, or the edge for low-latency inference. 
To learn more about the NGC Catalog content, visit the [NGC Catalog ](https://ngc.nvidia.com/) website. 
## [2. Terms and Concepts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#terms-and-concepts)
The following are common terms used in this document. 
Expand
Term| Definition  
---|---  
Authenticated / Registered User| A user who has signed in to NGC using their email account. The user inherits all "guest user" privileges and can access certain free/ free trial entities/features that require users to sign in.   
Container Images| All applications running in NGC are containerized as Docker containers and execute in our Runtime environment. Containers are stored in the NGC Registry nvcr.io, accessible from both the CLI and the Web UI.   
Container Port| Opening a port when creating a job will create a URL that can be used to reach the container on that port using web protocols. The security of web applications (for example, Jupyterlab) that are accessed this way is the user's responsibility. See note below.   
Enterprise Catalog|  The Enterprise Catalog includes the NVIDIA AI Enterprise software and can only be accessed by customers with an active subscription. NVIDIA AI Enterprise also includes software available in the public/free catalog which is designated as "NVIDIA AI Enterprise Supported."  The existing implementation of the enterprise catalog will be integrated with the NGC Catalog described in this document.   
Enterprise-only features| The features of the NGC Catalog that are only available for users with a product (that is, subscribers).   
Enterprise-only software | The containers, Helm charts, resources, models, and collections that are only available for users with an NVIDIA AI Enterprise subscription.   
Entity| A container, model, helm chart, or resource. They are also referred to as "software" in this document.   
Guest User| An unauthenticated user who can access (view and download) entities from the public catalog without signing in.   
Models| NGC offers a collection of state-of-the-art pre-trained deep learning models that can be easily used out of the box, re-trained or fine-tuned.   
NVIDIA AI Enterprise |  The software layer of the [NVIDIA AI](https://www.nvidia.com/en-us/ai-data-science/) platform, NVIDIA AI Enterprise, accelerates the data science pipeline and streamlines the development and deployment of production AI, including generative AI, computer vision, speech AI, and more. Regular security reviews, API stability, and dependable support SLAs ensure AI projects stay on track.  The NVIDIA AI Enterprise subscriptions include entities, support, and exclusive software features/models.   
Private Registry| The NGC private registry provides a secure space to store and share custom containers, models, resources, and Helm charts within your enterprise.   
Publisher| Publisher is an owner of the entity hosted on NGC.  
Resources| NGC offers step-by-step instructions and scripts for creating deep learning models that you can share within teams or the org.   
Subscriber|  A user who is signed in (registered), to NGC using their email account and is part of an org that has access to products (for example, "nv-ai-enterprise", "riva-enterprise").  An example of a free product for subscriber is someone who has purchased a license or has been granted access to gated software for free for a limited time.   
## [3. Why NGC Software](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#why-ngc-software)
NGC provides software to meet the needs of data scientists, developers, and researchers across various levels of AI expertise. 
All software hosted on NGC undergoes thorough scans for common vulnerabilities and exposures (CVEs), crypto, and private keys. 
In addition to security scanning, NGC software is tested against a wide range of GPU-enabled platforms, including public cloud instances, workstations, and OEM servers designed for data center or edge deployments. Supported GPUs include H100, V100, A100, T4, Jetson, and the RTX Quadro. 
NGC software is tested and assured to scale across multiple GPUs and, in some cases, across multiple nodes, ensuring users can fully utilize their GPU-powered servers out of the box. 
For select containers, NVIDIA offers NGC Support Services to run software on DGX platforms or certified OEM servers. The service gives enterprise IT direct access to NVIDIA subject matter experts to address software issues and minimize system downtime quickly. 
## [4. Accessing NGC Software](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#accessing-ngc-software)
There are four ways to explore and access software on NGC. 
**Guest Access** : Content under guest access does not require users to register or sign in to pull or download the software. 
Guest users can view all publicly available software and most of the entitled content in the NGC Catalog but cannot download entitled content. 
The majority of software on the NGC Catalog falls under guest access. However, it is important to note that many third-party applications require a license key that can be sourced directly from ISVs. While pulling public software from the NGC Catalog does not require sign-in, a user might have to reach out to an ISV to obtain a license key for further use. 
**Authenticated Access:** Software under authenticated access requires a user to [sign into their NGC org using an NVIDIA account](https://ngc.nvidia.com/signin) or sign in to NGC using SSO if the user's org is federated to their external SSO/IdP service. Pulling or downloading the software requires the user to provide their API key. 
Registered users can view and download all publicly available software in the NGC Catalog. Entitled content is also viewable but not downloadable. Note that registered users may not view content exclusively gated to users of that product. 
**Approved Access:** The publisher must grant user approval to access the software under this category. Once access is granted, the user will receive a notification with further instructions for accessing the software. Instructions to request access are provided in the overview section of the respective software. 
**Subscription:** To access subscription-based software, users must provide Business Address details and a token (serial number, activation code, and so on). Note that this category also requires Authenticated Access. 
Subscribers can view and download all publicly available software, including entitled content and exclusive content, in the NGC Catalog. 
The following table outlines the permissions and capabilities associated with each user access level (guest user, registered user, subscriber). 
Access Level| View Public Entities| Download Public Entities| View Entitled Content| Download Entitled Content| View/Download Exclusive Content  
---|---|---|---|---|---  
Guest User| Yes| Yes| Yes| No| No  
Registered User| Yes| Yes| Yes| No| No  
Subscriber| Yes| Yes| Yes| Yes| Yes  
## [5. Registering and Activating a New NGC Org to Obtain Authenticated Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#registering-activating-ngc-account)
Instructions for registering and activating a new NGC org. 
###  [5.1. Signing Up for an NVIDIA Cloud Account and Activating an Individual NGC Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#account-signup)
This section describes the steps to sign up for an NCA account and activate an individual NGC org. 
  1. Go to the [NGC sign-in page](http://ngc.nvidia.com/signin) from your browser, enter your email address, and then click **Continue**. 
![login-new-org.png](https://docscontent.nvidia.com/dims4/default/26f849d/2147483647/strip/true/crop/297x391+0+0/resize/297x391!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Flogin-new-org.png)
  2. In this step you will create your NVIDIA sign-in identity using NVIDIA's default IdP. At the **Create your Account** screen, create a password, make sure to review the NVIDIA Account Terms of Use and Privacy Policy, and click **Create Account** to accept and proceed with account creation. You will receive an email to verify your email address.
![create-an-account-dark.png](https://docscontent.nvidia.com/dims4/default/e36de8b/2147483647/strip/true/crop/668x633+0+0/resize/668x633!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fcreate-an-account-dark.png)
A verification email is sent to your email address.
![verify-email-dark.png](https://docscontent.nvidia.com/dims4/default/ef7cf3b/2147483647/strip/true/crop/669x464+0+0/resize/669x464!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fverify-email-dark.png)
  3. Open the NVIDIA account creation email and click **Verify Email Address.**
![account-created-email.png](https://docscontent.nvidia.com/dims4/default/06ec596/2147483647/strip/true/crop/605x628+0+0/resize/605x628!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Faccount-created-email.png)
You are automatically directed to nvidia.com and see an email verified successfully page. This window will close automatically 
![email-verified-dark.png](https://docscontent.nvidia.com/dims4/default/415c273/2147483647/strip/true/crop/685x293+0+0/resize/685x293!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Femail-verified-dark.png)
  4. At the **Almost done!** dialog, set your communications preferences, and then click **Submit**. 
![almost-done-dark-slim.png](https://docscontent.nvidia.com/dims4/default/9465471/2147483647/strip/true/crop/664x399+0+0/resize/664x399!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Falmost-done-dark-slim.png)
  5. Enter the password you just created to continue setting up your NVIDIA Cloud Account. (This is a required security measure). 
![ngc-sign-in-existing-user-dark.png](https://docscontent.nvidia.com/dims4/default/c019c4a/2147483647/strip/true/crop/371x421+0+0/resize/371x421!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-sign-in-existing-user-dark.png)
  6. Give your NVIDIA Cloud Account (NCA) a name that will help you identify it easily the next time you sign-in. 
![create-nvidia-cloud-account.png](https://docscontent.nvidia.com/dims4/default/e59e9a0/2147483647/strip/true/crop/387x466+0+0/resize/387x466!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fcreate-nvidia-cloud-account.png)
  7. Complete your user profile at the **Set Your Profile** screen, agree to the NVIDIA GPU Cloud Terms of Use, and then click **Submit**.
![set-your-profile.png](https://docscontent.nvidia.com/dims4/default/a79d973/2147483647/strip/true/crop/585x414+0+0/resize/585x414!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fset-your-profile.png)
Your NVIDIA account is created, and you are automatically redirected to your individual NGC org. 
![ngc-default-landing-page.png](https://docscontent.nvidia.com/dims4/default/d6f03f0/2147483647/strip/true/crop/906x477+0+0/resize/906x477!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-default-landing-page.png)
Your access to NVIDIA NGC org is completed, you can choose to complete the setup of your NVIDIA Cloud Account now, or at a later time. 


###  [5.2. NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-api-keys)
NVIDIA NGC API keys are required to authenticate with NGC services using NCG CLI, Docker CLI, or direct API requests. 
NGC provides two types of API keys:  

Personal Keys 
    
  * Any NGC org user can generate a personal key.
  * An NGC org user can grant a personal key up to the permissions assigned to them in the NGC org. 
  * A personal key is linked to the user’s NGC org lifecycle. 
    * If the user’s permissions change, the available permissions that can be or are assigned to the personal key also change. 
    * If the user is removed from the NGC org, the key's validity is revoked. 
  * Supports updating permissions, rotation, and deletion (immediate revocation). 
    * Org owners and user_admins can revoke any member’s key on demand. 
  * Each user can generate up to eight personal keys.


Use personal keys to begin using NGC services within your sandbox. Personal keys are best suited for individuals working on early development and testing code before moving to pre-production and production releases. 
To learn how to authorize the services you have access to in the org and generate a personal key, go to [Generating a Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-personal-api-key). 
Important:
Use the legacy NGC API Key to authenticate with Base Command Platform, Fleet Command, or other NGC services that don’t support "Personal key" authentication. For cross-org authorization, continue using the legacy NGC API Key. NVIDIA plans to deprecate the **legacy NGC API key** after 2025. NVIDIA encourages you to use the Personal Key, but if you need to continue using the legacy API key, go to [Generating a Legacy NGC API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-legacy-api-key "To generate a legacy API key, go to Setup > API Keys and click + Generate Legacy Key in the Legacy Keys drop-down.") to find out where to create a new one. Also, your current **NGC API key** will continue to work.  

Service Keys 
    
  * The lifecycle of service keys is linked to the NGC org account, not associated with an individual user. 
  * Only NGC org owners and user_admins can manage service keys.
  * A service key can be scoped to access only the permissions and services required, or full access to the services enabled in the org. 
  * Supports scoped permissions, updating permissions, on-demand revocation, rotation, and deletion. 
  * An NGC org can have up to 50 service keys.


Use service keys when you require automated communication between machines and deploying to pre-production and production environments where you do not want to depend on a user’s membership status in the NGC org. 
Note:
Service keys currently do not support listing artifacts in NGC CLI or Docker CLI. This functionality will be added in the future. In the meantime, use a Personal API key to list artifacts. 
**Examples using NGC API Keys**
Here are some examples of using NGC API keys to authenticate with NGC CLI and Docker CLI:  

NGC CLI 
    
Copy
Copied!
```
      
      
$ ngc config set 

    
```

Paste your key value at the API_KEY prompt:
Copy
Copied!
```
      
      
[Enter API key [****API-Key]. Choices: [<VALID_APIKEY>]

    
```
    
Important:
Always use the latest NGC CLI version to access the newest features, bug fixes, performance improvements, and security updates. Check for the latest versions at [NGC CLI Installers](https://org.ngc.nvidia.com/setup/installers/cli) or run `ngc version list` to view the latest releases, then upgrade using 
Copy
Copied!
```
      
      
ngc version upgrade

    
```


Docker CLI 
    
Copy
Copied!
```
      
      
docker login nvcr.io --username '$oauthtoken'

    
```

For the username, enter `'$oauthtoken'` exactly as shown. It is a special name that indicates that you will authenticate with an API key. Paste your key value at the Password prompt. 
###  [5.2.1. Supported NGC Applications and API Key Types](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-apps-api-keys)
The NVIDIA NGC applications/services that support Personal and Service Keys are listed below: 
NGC Application/Services| Service Description  
---|---  
NVIDIA NGC Catalog| Grants your key permission to access or download containers and artifacts from the NGC Catalog. The permission level matches your account's permissions for the catalog.   
NVIDIA NGC Private Registry | The key is authorized to perform actions on your organization's private registry service, such as pulling, retrieving, creating, or deleting containers and artifacts. The permission level assigned to the key matches the permission level of your user account. Therefore, your user account must have permissions for the Private Registry.   
NVIDIA Cloud Functions | This authorization allows your key to perform actions on your organization’s cloud functions service. If your organization has private functions published by NVIDIA, or if your cloud functions service enables you to create, deploy, and run your own functions, your personal key will have the same permissions as your user account for the cloud functions service. Therefore, it's important that your user account has the necessary permissions for Cloud Functions.   
NVIDIA Public API Endpoints| Grants permission for your key to access NVIDIA NIM inference endpoints listed in the [NVIDIA API Catalog](https://build.nvidia.com). Therefore, your user account must have Public API Endpoints permissions.   
NVIDIA Secrets Manager| Authorizes your key to perform actions on the NVIDIA Secrets Manager service, which is used to store and manage secrets. Your key will have the same permission level as your user account, so your user account must possess Secrets Manager permissions.   
###  [5.2.2. Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-api-key)
Generating API keys is essential for authenticating with NGC services using the NGC CLI, Docker CLI, or direct API requests. 
###  [5.2.2.1. Generating a Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-personal-api-key)
  1. Sign in to the NGC website. 
From a browser, go to <https://ngc.nvidia.com/signin> and then enter your email and password. 
  2. Click your user account icon in the top-right corner and select **Setup**.
![ngc-user-profile-menu-setup.png](https://docscontent.nvidia.com/dims4/default/6d2b485/2147483647/strip/true/crop/164x348+0+0/resize/164x348!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-user-profile-menu-setup.png)
  3. Click **Generate API Key** from the available options. 
![api-key-generate.png](https://docscontent.nvidia.com/dims4/default/6d6b0c2/2147483647/strip/true/crop/1296x665+0+0/resize/1296x665!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate.png)
  4. On the **Setup > API Keys** page, click **+ Generate Personal Key** on the menu or the pane. 
![api-key-generate-page.png](https://docscontent.nvidia.com/dims4/default/b7379b0/2147483647/strip/true/crop/1248x1527+0+0/resize/1248x1527!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-page.png)
  5. In the **Generate Personal Key** dialog, fill in the required information for your key.
![api-key-generate-personal-key-dialog.png](https://docscontent.nvidia.com/dims4/default/7f16c88/2147483647/strip/true/crop/467x431+0+0/resize/467x431!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-personal-key-dialog.png)
     * **Key Name** : Enter a unique name for your key. 
     * **Expiration** : Choose the expiration date for the key. 
![api-key-generate-personal-key-expiration.png](https://docscontent.nvidia.com/dims4/default/9f003a2/2147483647/strip/true/crop/327x289+0+0/resize/327x289!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-personal-key-expiration.png)
     * **Services Included** : Choose from the available services the key is permitted to access. Refer to [Assigning Services to Your Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#assigning-services-personal-api-key) to learn more about each service and when to assign service access to your Personal Key. 
  6. Click **Generate Personal Key** when finished.
Your API key appears in the following dialog. 
  7. NGC does not save your key, so store it securely. You can copy your API Key to the clipboard by selecting **Copy Personal Key** or using the copy icon to the right of the API key. 
![api-key-generate-personal-key-confirm.png](https://docscontent.nvidia.com/dims4/default/cf7f927/2147483647/strip/true/crop/374x288+0+0/resize/374x288!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-personal-key-confirm.png)
You can generate up to eight personal keys and manage them from the **Setup > Personal Keys** dashboard. To activate or deactivate a key, click the **Active** toggle. The **Actions** (ellipsis) menu allows you to rotate or delete a personal key. 
![api-key-generate-personal-key-dashboard.png](https://docscontent.nvidia.com/dims4/default/e6176b1/2147483647/strip/true/crop/1243x543+0+0/resize/1243x543!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-personal-key-dashboard.png)


###  [5.2.2.1.1. Assigning Services to Your Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#assigning-services-personal-api-key)
The services you can assign to a personal API key depend on two factors: 
  * The services enabled for the NGC org where you generate the API key. 
  * The service roles assigned to you by your NGC org owner or administrator. 


For example, consider an NGC org with the following services enabled: 
![ngc-org-subscriptions.png](https://docscontent.nvidia.com/dims4/default/a8a5b45/2147483647/strip/true/crop/879x669+0+0/resize/879x669!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-org-subscriptions.png)
An NGC user account might have the following access roles assigned: 
![ngc-user-account-example.png](https://docscontent.nvidia.com/dims4/default/42ceb1e/2147483647/strip/true/crop/278x387+0+0/resize/278x387!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-user-account-example.png)
In this scenario, the NGC org has enabled NVIDIA Microservices, Private Registry, NVIDIA AI Enterprise, and Cloud Functions (NVCF). The user account has been granted access roles for all these services. Therefore, a personal API key can be generated with permissions to access one or all of them. 
![ngc-generate-personal-key-dialog.png](https://docscontent.nvidia.com/dims4/default/da40c8d/2147483647/strip/true/crop/451x440+0+0/resize/451x440!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-generate-personal-key-dialog.png)
If a service is unavailable for assignment to the API key, it indicates that the org owner or administrator has not granted the user the necessary role for that service. 
For details about each service listed above and its function, see the table [Supported NGC Applications and API Key Types](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-apps-api-keys). 
###  [5.2.2.1.2. Generating a Legacy NGC API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-legacy-api-key)
To generate a legacy API key, go to **Setup** > **API Keys** and click **+ Generate Legacy Key** in the **Legacy Keys** drop-down. 
![api-key-legacy-key.png](https://docscontent.nvidia.com/dims4/default/c02d4db/2147483647/strip/true/crop/1220x661+0+0/resize/1220x661!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-legacy-key.png)
In the **Generate Legacy Key** dialog, click on **+ Generate Legacy Key**. 
![api-key-generate-legacy-key.png](https://docscontent.nvidia.com/dims4/default/9c1eae9/2147483647/strip/true/crop/1129x592+0+0/resize/1129x592!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-generate-legacy-key.png)
###  [5.2.2.2. Generating a Service API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-service-api-key)
  1. Sign in to the NGC website. 
From a browser, go to <https://ngc.nvidia.com/signin> and then enter your email and password. 
  2. Select **Organization** from the user account menu on the upper right. 
![ngc-catalog-user-account-menu-org.png](https://docscontent.nvidia.com/dims4/default/9b1eabd/2147483647/strip/true/crop/1999x949+0+0/resize/1440x684!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-catalog-user-account-menu-org.png)
Select **Service Keys** on the organization dashboard. 
![ngc-org-dashboard-service-keys.png](https://docscontent.nvidia.com/dims4/default/e15c3d2/2147483647/strip/true/crop/1185x590+0+0/resize/1185x590!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fngc-org-dashboard-service-keys.png)
  3. On the **Organization > Service Keys** page, click **+ Create Service Key** button to create a key.
![api-key-create-service-key-page.png](https://docscontent.nvidia.com/dims4/default/ba9cbec/2147483647/strip/true/crop/1184x490+0+0/resize/1184x490!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-page.png)
  4. In the **Create Service Key** dialog, fill in the required configuration. Service keys currently support services such as NVIDIA NIM, NGC Catalog, and Private Registry. Assign scopes and resource permissions to the key.
![api-key-create-service-key-form.png](https://docscontent.nvidia.com/dims4/default/02e1526/2147483647/strip/true/crop/1999x907+0+0/resize/1440x653!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-form.png)
In the **Entity Type** field, select from the available options to grant to the API key. 
![api-key-create-service-key-entity-type.png](https://docscontent.nvidia.com/dims4/default/8467f41/2147483647/strip/true/crop/1999x1067+0+0/resize/1440x769!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-entity-type.png)
In the **Scope** field, choose from the available options. 
![api-key-create-service-key-scope.png](https://docscontent.nvidia.com/dims4/default/9d8d272/2147483647/strip/true/crop/1999x994+0+0/resize/1440x716!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-scope.png)
  5. Click **Next Step** to review your key configuration.
![api-key-create-service-key-form-next-step.png](https://docscontent.nvidia.com/dims4/default/dc3aee3/2147483647/strip/true/crop/1999x900+0+0/resize/1440x648!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-form-next-step.png)
  6. Once you verified the configuration, click **Confirm** to generate your service key. Your service key appears in the next dialog. 
![api-key-create-service-key-confirm.png](https://docscontent.nvidia.com/dims4/default/2d91eb0/2147483647/strip/true/crop/1999x975+0+0/resize/1440x702!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-confirm.png)
  7. NGC does not save your key, so store it securely. You can copy your API Key to the clipboard by clicking the copy icon to the right of the API key or the **Copy Service Key** button. 
![api-key-create-service-key-copy-key.png](https://docscontent.nvidia.com/dims4/default/0a80974/2147483647/strip/true/crop/1999x887+0+0/resize/1440x639!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-copy-key.png)
Make sure to copy the key value before leaving this page. Once you navigate away, the key value cannot be retrieved, and replacing it will require generating a new key. 
NGC supports multiple Service API keys, which are managed from the **Organization > Service Keys** dashboard. 
To activate or deactivate a key, click the **Active** toggle. The **Actions** (ellipsis) menu allows you to rotate or delete a service key. 
![api-key-create-service-key-dashboard.png](https://docscontent.nvidia.com/dims4/default/0736ea0/2147483647/strip/true/crop/1182x309+0+0/resize/1182x309!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fcommon%2Fgraphics%2Fgraphics-ngc%2Fapi-key-create-service-key-dashboard.png)
Note:
When managing containers, ensure the scopes **Get Container** and **Get Container list** are assigned to your service key. For other types of artifacts, add the **Get Artifact** and **Get Artifact list** scopes. These scopes are the minimum required to discover the artifacts that need to be managed. Refer to the [NGC Catalog User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html) and [Private Registry User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html) for more information. 


## [6. Introduction to the NGC Catalog and NGC CLIs](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#intro-to-ngc-cli)
**Unified NGC and Enterprise Catalog**
Note:
The Enterprise Catalog, formerly a separate repository for NVIDIA AI Enterprise-supported software, is now integrated into the public NGC Catalog, providing a unified and comprehensive platform. NVIDIA AI Enterprise customers can access their exclusive software and features within the NGC Catalog using their active entitlements. 
The NGC Catalog aims to provide a centralized catalog of publicly available entities (e.g., containers, models, resources) alongside those that are part of products called _entitled_ entities. This approach enables users to search and filter seamlessly across all entities, for a more efficient and improved user experience. 
Users can view and download entitled entities by signing in to NGC. The NGC CLI is also available for downloading software using the API key. Access to all granted products will remain even when switching org/team context. Unauthenticated users will see a prompt to log in or gain access to the product when attempting to download gated features or entitled entities. 
Publishers can publish and map entities to products. Access to entities is restricted by entity type, entity access type, user subscriptions, and roles, enhancing security and control. For entitled entities, guest users are encouraged to convert to registered or subscribed status to access product-specific entities. 
**Introduction to NGC CLIs**
The NGC CLIs are command-line interfaces for managing content within the NGC Registry. The CLI operates within a shell and lets you use scripts to automate commands. 
**NGC Catalog CLI**
The NGC Catalog CLI is available to you if you have guest access to the NGC Registry, and with it, you can 
  * View a list of GPU-accelerated Docker container images, pre-trained deep-learning models, and scripts for creating deep-learning models. 
  * Download container images, models, and resources. 


**NGC Registry CLI**
The NGC Registry CLI is available to you if you are logged in with your own NGC account or with an NGC Private Registry account, and with it, you can 
  * View a list of GPU-accelerated Docker containers available and detailed information about each image. 
  * See a list of deep-learning models and resources and detailed information about them. 
  * Download container images, models, and resources.
  * Upload container images, models, and resources.
  * Create and manage users and teams (available to NGC Private Registry administrators). 


For more details and best practices, visit the [NGC CLI documentation page](https://docs.ngc.nvidia.com/cli/index.html). 
###  [6.1. Installing NGC Catalog CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#installing-ngc-catalog-cli)
To install NGC Catalog CLI, 
  1. Enter the NGC website (<https://ngc.nvidia.com>) as a guest user.
  2. In the top right corner, click **Welcome Guest** and then select **Setup** from the menu.
  3. Click **Downloads** under **CLI** from the Setup page.
  4. From the CLI Install page, click the **Windows** , **Linux** , or **macOS** tab, according to the platform you will be running NGC Catalog CLI.
  5. Follow the instructions to install the CLI.
  6. Verify the installation by entering `ngc --version`. The output should be `NGC CLI x.y.z` where x.y.z indicates the version. 


###  [6.2. Installing NGC Registry CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#installing-ngc-registry-cli)
To install NGC Registry CLI, 
  1. Log in to your enterprise account on the NGC website (<https://ngc.nvidia.com>).
  2. In the top right corner, click your user account icon and select **Setup** , then click **Downloads** under **CLI** from the Setup page.
  3. From the CLI Install page, click the **Windows** , **Linux** , or **macOS** tab, according to the platform from which you will be running NGC Registry CLI.
  4. Follow the instructions to install the CLI.
  5. Verify the installation by entering `ngc --version`. The output should be `NGC CLI x.y.z` where x.y.z indicates the version. 


## [7. Docker Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvcontainers)
Over the last few years there has been a dramatic rise in the use of software containers for simplifying deployment of data center applications at scale. Containers encapsulate an application along with its libraries and other dependencies to provide reproducible and reliable execution of applications and services without the overhead of a full virtual machine. 
GPU support within Docker containers enables GPU-based applications that are portable across multiple machines in a similar way to how Docker enables CPU-based applications to be deployed across multiple machines.  

Docker container 
     A Docker container is an instance of a Docker image. A Docker container deploys a single application or service per container.  

Docker image 
     A Docker image is simply the software (including the filesystem and parameters) that you run within a Docker container. 
###  [7.1. What Is a Docker Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#whatiscont)
A Docker container is a mechanism for bundling a Linux application with all of its libraries, data files, and environment variables so that the execution environment is always the same, on whatever Linux system it runs and between instances on the same host. 
Unlike a VM which has its own isolated kernel, containers use the host system kernel. Therefore, all kernel calls from the container are handled by the host system kernel. Users can use Docker containers as the mechanism for deploying deep learning frameworks on-prem,, in the cloud, or at the edge. 
A Docker container is the running instance of a [Docker image](https://docs.docker.com/engine/getstarted/step_four/). 
###  [7.2. Why Use A Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#whycont)
Using containers allows you to package your application, dependencies, and environment variables into a single image rather than on each system you run on. Additional benefits to using containers include: 
  * Multiple versions of the same application, which may have conflicting software dependencies, can run on the same server. 
  * Containerized applications can be deployed on premise, in the cloud, or at the edge 
  * Specific GPU resources can be allocated to a container for isolation and better performance. 
  * Easily share, collaborate, and test applications across different environments. 
  * Resolve network-port conflicts between applications by mapping container-ports to specific externally-visible ports when launching the container. 


###  [7.3. Searching and Filtering Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-containers)
To view NGC containers, navigate to **Catalog** > **Containers** in the left menu. Use the search bar at the top of the page to find a particular container or sort the list using the criteria from the dropdown menu. You can refine your search by utilizing the filters under NVIDIA Platform, NVIDIA AI Enterprise, Quick Deploy, and many others. The descriptions for the filtering options are as follows: 
  * **Use Case** : Choose from the available common use cases. 
  * **NVIDIA Platform** : Choose from Clara, DeepStream, TensorFlow, and many others. 
  * **NVIDIA AI Enterprise Support:** Select this option to find publicly available containers supported by NVIDIA AI Enterprise containers. 


  * **NVIDIA AI Enterprise Exclusive** : Choose products under this to see entitled entities. 


  * **Quick Deploy** : Select this option to find containers to quickly deploy your artifacts in a Jupyter environment. 


  * **Industry** : Select by available industries. 


  * **Solution** : Select the solution that closely matches your use case. 


  * **Publisher** : Filter by publisher. 


  * **Architecture** : Choose this option for multi-architecture support. 


  * **Signed Images** : Choose this option for container images with a digital signature. 


  * **Multi-Node** : Choose this option for multi-node support. 


  * **Other** : Miscellaneous options. 


The following page displays a list of sample containers for guest users: 
![ngc-catalog-containers-guest.png](https://docscontent.nvidia.com/dims4/default/c9cd0cb/2147483647/strip/true/crop/1200x958+0+0/resize/1200x958!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-guest.png)
Select a container from the list to view its details. All users can access the overview information, regardless of their sign-in status. Here's an example of an **NVIDIA AI Enterprise Supported** container: 
![ngc-catalog-containers-nvaie-supported-example.png](https://docscontent.nvidia.com/dims4/default/ee99add/2147483647/strip/true/crop/1184x886+0+0/resize/1184x886!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example.png)
Users must sign in to view the content for the **Security Scanning** tab. 
![ngc-catalog-containers-nvaie-supported-example-security-tab.png](https://docscontent.nvidia.com/dims4/default/9d428e2/2147483647/strip/true/crop/1125x501+0+0/resize/1125x501!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-security-tab.png)
Similarly, when filtering on **NVIDIA AI Enterprise Essentials** , the available containers will be displayed: 
![ngc-catalog-containers-nvaie-supported-example-filtered.png](https://docscontent.nvidia.com/dims4/default/de166de/2147483647/strip/true/crop/1056x963+0+0/resize/1056x963!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-filtered.png)
Once you choose a container, it shows the information in the **Overview** tab: 
![ngc-catalog-containers-nvaie-supported-example-overview.png](https://docscontent.nvidia.com/dims4/default/e874e5b/2147483647/strip/true/crop/1022x560+0+0/resize/1022x560!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-overview.png)
If users are not subscribed to **NVIDIA AI Enterprise Software Exclusive** products, they’ll see the following message when viewing other tabs: 
![ngc-catalog-containers-nvaie-supported-example-unsubscribed.png](https://docscontent.nvidia.com/dims4/default/ec283c9/2147483647/strip/true/crop/1036x507+0+0/resize/1036x507!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-unsubscribed.png)
If users try to download the container, they’ll see a message indicating that a subscription is required: 
![ngc-catalog-containers-nvaie-supported-example-sub-req.png](https://docscontent.nvidia.com/dims4/default/d3eda97/2147483647/strip/true/crop/1038x636+0+0/resize/1038x636!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-sub-req.png)
However, once users subscribe to **NVIDIA AI Enterprise Software Exclusive** products, they can view the container information. 
![ngc-catalog-containers-nvaie-supported-example-subscribed.png](https://docscontent.nvidia.com/dims4/default/c6fdc9b/2147483647/strip/true/crop/1461x701+0+0/resize/1440x691!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-nvaie-supported-example-subscribed.png)
## [8. NGC Container Images in NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-catalog-containers)
NGC Containers are designed to enable a software platform centered around minimal OS requirements, Docker and driver installation on the server or workstation, and provisioning of all application and SDK software in the NGC containers through the NGC container registry. 
NGC Catalog is a curated set of fully integrated and optimized container images for Deep Learning, HPC and Visualization applications. 
  * Deep learning framework containers that take full advantage of NVIDIA GPUs in both single GPU and multi-GPU configurations. They include CUDA Toolkit, DIGITS workflow, and deep learning frameworks: NVCaffe, Caffe2, Microsoft Cognitive Toolkit (CNTK), MXNet, PyTorch, TensorFlow, Theano, and Torch. These framework containers are delivered ready-to-run, including all necessary dependencies such as CUDA runtime, NVIDIA libraries, and an operating system. NVIDIA updates these deep learning containers monthly to ensure they continue to provide peak performance. 
  * NGC also hosts a catalog of HPC applications such as NAMD, GROMACS, LAMMPS, RELION, CHROMA, MILC, and many more. 
  * In addition to HPC applications, NGC hosts the industry’s leading visualization tools, including ParaView with NVIDIA IndeX volume renderer, NVIDIA OptiX ray-tracing library, and NVIDIA Holodeck for interactive real-time visualization and high-quality visuals. 
  * NGC also hosts popular third-party GPU-ready application containers which conform to NGC container standards and best practices, making it easy to get the most out of your NVIDIA GPU. 
  * With the NGC Quick Deploy feature, many NGC containers can be used as a kernel to launch a JupyterLab instance on Google Cloud Vertex AI Workbench with optimal configuration and all software dependencies preload. 


###  [8.1. Why NGC Container Images?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#why-ngc-container-images)
Every image hosted on NGC Catalog undergoes a security scan and GPU-performance test by the NGC team. 
###  [8.1.1. NGC Container Security Policy](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-container-security-policy)
A critical function of enterprise risk and security assessment processes is to ensure all container images being used in development or deployment have been tested for known vulnerabilities. Containers published to the NGC Catalog undergo scanning with the NGC Container Security Policy. 
The security scans include checks such as the following: 
  * _Outdated software packages, such as vulnerability scans_
  * _Metadata checks, such as open ports specified in Dockerfiles, etc_
  * _Cryptographic key material leaks_


The scanning policy for CVEs rates the severity into critical, high, medium, and low vulnerabilities using the Common Vulnerability Scoring System (CVSS). Scan results and NVIDIA Security-Risk Scale are made available to users. Published images are rescanned every 30 days to reflect the newest CVE findings. 
###  [8.1.2. NVIDIA Security Risk Scale](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-security-risk-scale)
The NVIDIA Security-Risk Scale rates the risk level a given container image poses for a development/production infrastructure environment. 
This rating takes into account vulnerability scans for OS and non-OS packages. 
Scale| Description| Packages| Details  
---|---|---|---  
AAA| Rated to have lowest security risk.| 0| No package with vulnerabilities  
AA| Rated to have lower security risk.| 1| 1 package has a Critical or High vulnerability   
A| Rated to have moderate security risk with some speculative judgment needed based on environment workloads | 2-3| 2-3 packages with Critical or High vulnerabilities   
B| Rated to have high security risk with some speculative judgment needed based on environment workloads | 3+| 4-5 packages with Critical or High vulnerabilities   
C| Rated as highest security risk | 5+| 5+ packages with Critical or High vulnerabilities   
###  [8.1.3. GPU-performance tests for NGC Catalog Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-performance-test)
To ensure that NVIDIA GPU owners can perform well with NGC hosted images, all container images undergo basic installation, functional, scalability and performance tests on GPUs. 
These tests are performed on an array of GPUs ranging from NVIDIA T4s to A100 to DGX Systems for performance and multi-GPU for scale. The selection of supported GPUs may be limited to few architectures or single-/multi-GPU based on the business use case of application containers. 
These tests are performed on both bare-metal installations and cloud deployed instances to ensure both on-prem and cloud deployment use-cases. 
###  [8.2. NVIDIA Container Toolkit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-container-toolkit)
The NVIDIA Container Toolkit allows users to build and run GPU accelerated containers. The toolkit includes a container runtime [library](https://github.com/NVIDIA/libnvidia-container) and utilities to automatically configure containers to leverage NVIDIA GPUs. It integrates with many popular container runtimes including Docker, podman, CRI-O, LXC etc. 
To enable portability in Docker images that leverage NVIDIA GPUs, NVIDIA developed [nvidia-docker](https://github.com/NVIDIA/nvidia-docker), an open-source project hosted on Github that provides the two critical components needed for portable GPU-based containers: 
  1. Driver-agnostic CUDA images.
  2. A Docker command line wrapper that mounts the user mode components of the driver and the GPUs (character devices) into the container at launch. 


`nvidia-docker` is a Docker command line wrapper that provisions a container with the necessary components to execute code on the GPU. 
When working with containers that utilize GPUs, the only command that must be executed through an `nvidia-docker`command is the `run` command. For all other functionalities, `docker` commands can be used. 
But for simplicity in this documentation we use `nvidia-docker` for all commands. 
###  [8.3. NVIDIA CUDA Toolkit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#cuda-toolkit-file)
The NVIDIA® CUDA® Toolkit provides a development environment for creating high-performance GPU-accelerated applications. With the CUDA Toolkit, you can develop, optimize, and deploy your applications on GPU-accelerated embedded systems, desktop workstations, enterprise data centers, cloud-based platforms, and HPC supercomputers. The toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler and a runtime library to deploy your application. 
GPU-accelerated CUDA libraries enable drop-in acceleration across multiple domains such as linear algebra, image and video processing, deep learning, and graph analytics. For developing custom algorithms, you can use available integrations with commonly used languages and numerical packages as well as well-published development APIs. Your CUDA applications can be deployed across all NVIDIA GPU families available on premise and on GPU instances in the cloud. Using built-in capabilities for distributing computations across multi-GPU configurations, scientists and researchers can develop applications that scale from single GPU workstations to cloud installations with thousands of GPUs. 
###  [8.4. Running Singularity Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity)
NGC supports both Docker and Singularity container runtimes. While Docker is prevalent primarily in enterprises, Singularity has become ubiquitous in the HPC community. Singularity was developed to better satisfy the requirements of HPC users and system administrators, including the ability to run containers without superuser privileges. 
NGC containers can be easily used with Singularity. Let’s use the[ NGC NAMD container](https://ngc.nvidia.com/catalog/containers/hpc:namd) to illustrate. NAMD is a parallel molecular dynamics application designed for high-performance simulation of large biomolecular systems, developed by the Theoretical and Computational Biophysics Group at the University of Illinois. 
###  [Prerequisites](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites)
These instructions assume the following. 
  * You have Singularity **v2.6+**[installed](http://github.com/sylabs/singularity) on your system 
  * You have performed the following steps from the NGC website. 
    * Signed up for an NGC account at <https://ngc.nvidia.com/signup>. 
    * Created an NGC API key for access to the NGC container registry
    * Browsed the NGC website and identified an available NGC container and tag to run
  * Ensure you have correctly set udev rules which are detailed ([here](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#runfile-verifications)) 


Note:
It is recommended that you install `nvidia-container-cli` because if installed, Singularity will use it. More information can be found [here](https://github.com/NVIDIA/nvidia-container-runtime). 
###  [8.4.2. Converting to Singularity Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#converting-to-singularity-image)
Before running with Singularity you must set NGC container registry authentication credentials. 
This is most easily accomplished by setting the following environment variables. 
bash 
Copy
Copied!
```
      
      
$ export SINGULARITY_DOCKER_USERNAME='$oauthtoken'
$ export SINGULARITY_DOCKER_PASSWORD=<NVIDIA NGC API key>

    
```

tcsh 
Copy
Copied!
```
      
      
> setenv SINGULARITY_DOCKER_USERNAME '$oauthtoken'
> setenv SINGULARITY_DOCKER_PASSWORD <NVIDIA NGC API key>

    
```

More information describing how to obtain and use your NVIDIA NGC API key can be found [here](https://docs.nvidia.com/ngc/ngc-user-guide/index.html). 
Once credentials are set in the environment, the NGC container can be pulled to a local Singularity image. 
Copy
Copied!
```
      
      
$ singularity build <app_tag>.simg docker://nvcr.io/<repository>/<app:tag>

    
```

This will save the container to the current directory as 
Copy
Copied!
```
      
      
<app_tag>.simg

    
```

For example to convert the HPC application NAMD hosted on NGC to a Singularity image, run 
Copy
Copied!
```
      
      
$ singularity build namd_2.12-171025.simg docker://nvcr.io/hpc/namd:2.12-171025

    
```

After the build has finished the Singularity image file, namd_2.12-171025.simg, will be available for use in the current working directory. 
###  [8.4.3. Running the Singularity Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#running-the-singularity-container)
Once the local Singularity image has been pulled, the following modes of running are supported. 
  * [Command line execution with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-command-line)
  * [Interactive shell with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-interactive-shell)


To leverage NVIDIA GPUs, you must use the Singularity flag `--nv`when running the containers. More singularity flags are explained [here](http://singularity.lbl.gov/action-flags). 
Important:
**For Amazon Machine Image Users** Amazon Machine Images on Amazon Web Service have a default root umask of 077. Singularity must be installed with a umask of 022 to run properly. To (re)install Singularity with correct permissions: 
  * Uninstall Singularity (if it is installed)
  * Change the umask with: `$ umask 0022`
  * Install Singularity
  * Restore the umask: `$ umask 0077`


This causes installed Singularity files to have permission 0755 instead of the default 0700. Note that the umask command only applies changes to the current shell. Use umask and install Singularity from the same shell session. 
###  [8.4.3.1. Directory Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-directory-access)
Singularity containers are themselves ostensibly read only. In order to provide application input and persist application output we’ll bind a host directory into our container, this is accomplished through the Singularity `-B` flag. The format of this flag is `-B <host_src_dir>:<container_dst_dir>`. Once a host directory is bound into the container we can interact with this directory from within the container exactly as we can outside the container. 
It is also often convenient to use the `--pwd <container_dir>` flag, which will set the present working directory of the command to be run within the container. 
The Singularity commands below will mount the present working directory on the host to `/host_pwd` in the container process and set the present working directory of the container process to `/host_pwd`. With this set of flags the `<cmd>` to be run will be launched from the host directory Singularity was called from. 
Copy
Copied!
```
      
      
$ singularity exec --nv -B $(pwd):/host_pwd --pwd /host_pwd <image.simg> <cmd>

    
```

Note:
Binding to a directory which doesn't exist within the container image requires kernel and configuration support that may not be available on all systems, particularly those running older kernels such as CentOS/RHEL 6. When in doubt contact your system administrator. 
###  [8.4.3.2. Command Line Execution with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-command-line)
Running the container with Singularity from the command line looks similar to the command below. 
Copy
Copied!
```
      
      
$ singularity exec --nv <app_tag>.simg <command_to_run>

    
```

For example, to run the NAMD executable in the container 
Copy
Copied!
```
      
      
$ singularity exec --nv namd_2.12-171025.simg /opt/namd/namd-multicore

    
```

###  [8.4.3.3. Interactive Shell with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-interactive-shell)
To start a shell within the container, run the command below 
Copy
Copied!
```
      
      
$ singularity exec --nv <app_tag>.simg /bin/bash

    
```

For example, to start an interactive shell in the NAMD container 
Copy
Copied!
```
      
      
$ singularity exec --nv namd_2.12-171025.simg

    
```

## [9. Prerequisites for Using NGC Catalog Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-image-prerequisites)
To enable portability in Docker images that leverage GPUs, three methods of providing GPU support for Docker containers have been developed. 
  * Running Docker-ce 19,.03 or later for Native GPU support 
  * `nvidia-docker2`
  * `nvidia-docker`


Each of these methods mount the user mode components of the NVIDIA driver and the GPUs into the Docker container at launch. They allow NGC containers to take full advantage of NVIDIA GPUs. 
###  [9.1. Prerequisites for Using NGC Containers on DGX Systems](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-dgx)
DGX™ users should follow the instructions in the [Preparing Your DGX System For Use With NVIDIA Container Runtime](https://docs.nvidia.com/deeplearning/frameworks/preparing-containers/index.html#prepare_dgx_system). 
###  [9.2. Prerequisites for Using NGC Containers on Cloud Platforms](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-csp)
On each of the major public cloud providers, NVIDIA publishes customized virtual machine images (VMIs) with updated OS’s and NVIDIA driver that have been tested with NGC containers. These VMIs have the NVIDIA Container Toolkit pre-installed allowing you to begin pulling and running Docker containers from NGC right away. To use the NVIDIA NGC GPU-optimized VMIs on cloud platforms, you would need - 
  * A cloud platform account with permissions to create resources. See the details for your public cloud: 
    * Alibaba - <https://home-intl.console.aliyun.com/>
    * AWS - [https://aws.amazon.com](https://aws.amazon.com/)
    * Microsoft Azure - [https://portal.azure.com](https://portal.azure.com/)
    * Google Cloud Platform (GCP) - <https://console.cloud.google.com/>


  * A CLI for respective cloud platforms if you wish to interface with your VM via a CLI 
    * [Alibaba Cloud CLI](https://www.alibabacloud.com/help/product/29991.htm)
    * [AWS CLI Version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
    * [Azure CLI 2.0](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
    * [gcloud SDK](https://cloud.google.com/sdk/docs/quickstarts)
  * Windows Users: Any CLI code snippets in the docs are for bash on Linux or Mac OS X. If you are using Windows and want to use the snippets as-is, you can [set up the Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about?redirectedfrom=MSDN) and use the bash shell (you will be in Ubuntu Linux). 


###  [9.3. Prerequisites for Using NGC Containers on Other NVIDIA GPUs](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-gpu)
  * Users running NGC containers on other NVIDIA GPUs or in a virtual GPU environment should follow the corresponding instructions for [TITAN PCs, Quadro PCs](https://docs.nvidia.com/ngc/ngc-titan-setup-guide/index.html), or [vGPUs](https://docs.nvidia.com/ngc/ngc-vgpu-setup-guide/index.html). 
  * Other users should follow the nvidia-docker installation documentation at [nvidia-docker _installation_](https://github.com/NVIDIA/nvidia-docker/wiki/Installation) and install the latest NVIDIA drivers for your GPU product type and series for your operating system. If NVIDIA drivers are not already configured on your system, then install them from here: [Download Drivers](http://www.nvidia.com/Download/index.aspx). 
  * Ensure you have an NVIDIA GPU supporting Compute Unified Device Architecture® (CUDA) version with compute capability 6.0.0 or higher. For example, Pascal GPU architecture generation or later. 


###  [9.4. HPC Visualization Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-container)
In addition to accessing the [NVIDIA optimized frameworks](http://docs.nvidia.com/deeplearning/dgx/index.html) and HPC containers, the NVIDIA GPU Cloud (NGC) container registry also hosts the following scientific visualization containers for HPC. These containers rely on the popular scientific visualization tool called [ParaView](https://www.paraview.org/). Visualization in an HPC environment typically requires remote visualization, that is, data resides and is processed on a remote HPC system or in the cloud, and the user graphically interacts with this application from their workstation. As some visualization containers require specialized client applications, the HPC visualization containers consist of two components:  

Server container 
     The server container needs access to the files on your server system. Details on how to grant this access are provided below. The server container can run both in serial mode or in parallel. For this alpha release, we are focusing on the serial node configuration. If you are interested in parallel configuration, contact hpcviscontainer@nvidia.com.  

Client container 
     To ensure matching versions of the client application and the server container, NVIDIA provides the client application in a container. Similarly, to the server container, the client container needs access to some of the ports to establish connection with the server container. 
In addition, the client container needs access to the users’ X server for displaying the graphical user interface. 
###  [9.4.1. Prerequisites For HPC Visualization Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-prereq)
  * Install [docker-ce](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/) and [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/tree/2.0). First install [docker-ce](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/), then install [nvidia-docker2](https://github.com/NVIDIA/nvidia-docker/tree/2.0) for your operating system and Docker version. For a script to install nvidia-docker2, see [Installing NVIDIA Docker 2.0](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-docker2). 
Note:
If you already have `nvidia-docker1` installed and intend to keep it, you can install `nvidia-container-runtime`. 
  * Install the NVIDIA Display driver version 384.57 or onwards depending on your GPU product type and series for your operating system. For more information, see [Download Drivers](http://www.nvidia.com/Download/index.aspx). 
  * Ensure you have an NVIDIA GPU supporting Compute Unified Device Architecture® (CUDA) version with compute capability 6.0.0 or higher. For example, Pascal GPU architecture generation or later. 
  * Log into the NVIDIA® GPU Cloud (NGC) Container Registry located at `nvcr.io` using your NGC API key. For step-by-step instructions on how to gain access and get your API key, see [Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-api-key). 


###  [9.4.2. Installing NVIDIA Docker 2.0](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-docker2)
The following script installs NVIDIA Docker 2.0 which is a prerequisite to pulling the ParaView with NVIDIA IndeX HPC visualization container. 
Full support for concurrent graphics and compute capabilities in containers is supported in NVIDIA Docker 2.0. Current installations of NGC run on NVIDIA Docker 1.0. Prior to using a container on any of these instances, NVIDIA Docker 2.0 must be installed. Use the following script below to install NVIDIA Docker 2.0 on your instance. 
Copy
Copied!
```
      
12345678910111213141516

      
# Install NVIDIA Docker 2.0
docker volume ls -q -f driver=nvidia-docker | \
 xargs -r -I{} -n1 docker ps -q -a -f volume={} | xargs -r docker rm -f
sudo apt-get purge -y nvidia-docker
curl -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
sudo tee /etc/apt/sources.list.d/nvidia-docker.list <<< \
"deb https://nvidia.github.io/libnvidia-container/ubuntu16.04/amd64 /
deb https://nvidia.github.io/nvidia-container-runtime/ubuntu16.04/amd64 /
deb https://nvidia.github.io/nvidia-docker/ubuntu16.04/amd64 /"
sudo apt-get -y update
sudo apt-get install -y nvidia-docker2
sudo pkill -SIGHUP dockerd
# Tests
#docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi

    
```

###  [9.4.3. ParaView With NVIDIA Holodeck](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-holodeck)
Currently, the ParaView with NVIDIA Holodeck container requires a running X server both on the server host and the client host. Therefore, only a single container image is required. 
  1. Create X-forwarding variables for your container.
Copy
Copied!
```
      
      
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth;
touch /tmp/.docker.xauth;
xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f /tmp/.docker.xauth nmerge -

    
```

  2. On the server host, start the ParaView Holodeck server:
Copy
Copied!
```
      
      
docker run --rm -it --runtime=nvidia \
-v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
-e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
-p 11111:11111 \
--shm-size=4g \
nvcr.io/nvidia-hpcvis/paraview-holodeck:glx-17.11.13-beta \
./service.sh externalvis pvserver

    
```

The Holodeck render window showing a space scene displays. 
The server container is ready after you receive a message similar to the following: 
Copy
Copied!
```
      
      
"Accepting connection(s): [...]:11111"

    
```

  3. Set up X access and start the client container on the client host. Ensure you replace `your_server_hostname`. 
Copy
Copied!
```
      
      
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth 
touch /tmp/.docker.xauth
xauth nlist :0 | sed -e 's/^..../ffff/' \
| xauth -f /tmp/.docker.xauth nmerge -docker run --rm -it --runtime=nvidia \
-v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
-e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
nvcr.io/nvidia-hpcvis/paraview-holodeck:glx-17.11.13-beta \
sh -c paraview\ --server-url=cs://your_server_hostname:11111

    
```

The ParaView user interface displays. 


###  [9.4.4. ParaView With NVIDIA IndeX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index)
To support both X-enabled and headless hosts, the ParaView IndeX container image is available with GLX and EGL support. The following section shows how to launch the IndeX container with different use cases. 
For more information about ParaView, see the [ParaView User’s Guide](https://www.paraview.org/paraview-guide/) and the [NVIDIA IndeX SDK](https://developer.nvidia.com/index). 
###  [9.4.4.1. Single-Machine With GLX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-single)
  1. Login to the docker repository and pull the X display-enabled container on your workstation:
Copy
Copied!
```
      
      
docker pull nvcr.io/nvidia-hpcvis/paraview-index:glx-17.11.13-beta

    
```

  2. Specify X-forwarding variables:
Copy
Copied!
```
      
      
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth
touch /tmp/.docker.xauth
xauth nlist :0 | sed -e 's/^..../ffff/' \
| xauth -f /tmp/.docker.xauth nmerge

    
```

  3. Run the image. In this example, host system data in the current directory $(pwd) are mounted to both /work in the container. This should be modified as desired by the user. 
Copy
Copied!
```
      
12345

      
docker run --rm -it --runtime=nvidia \
-v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
-v $(pwd):/work -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
nvcr.io/nvidia-hpcvis/paraview-index:glx-17.11.13-beta \
sh -c paraview

    
```



###  [9.4.4.2. Server Container With EGL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-server)
In a typical client-server setup, one container acting as the server will run remotely on a display-less machine, connected to a second container that runs locally on a workstation and provides the graphical front end. Use the following command to pull the EGL-enabled, no-display container from the NGC registry on the server host: 
Copy
Copied!
```
      
1

      
docker pull nvcr.io/nvidia-hpcvis/paraview-index:egl-17.11.13-beta

    
```

Run the server component on the server host. We listen on the default port 11111: 
Copy
Copied!
```
      
12

      
docker run --runtime=nvidia -p 11111:11111 --rm -it \
nvcr.io/nvidia-hpcvis/paraview-index:egl-17.11.13-beta sh -c pvserver

    
```

###  [9.4.4.3. GLX Client Connecting To A Server](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-client)
Pull the X display-enabled container on your workstation: 
Copy
Copied!
```
      
      
docker pull nvcr.io/nvidia-hpcvis/paraview-index:glx-17.11.13-beta

    
```

Set up X access and launch the client application container (make sure to replace your_server_hostname with the address of your ParaView server host): 
Copy
Copied!
```
      
      
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth
touch /tmp/.docker.xauth
xauth nlist :0 | sed -e 's/^..../ffff/' \
| xauth -f /tmp/.docker.xauth nmerge -

    
```

Copy
Copied!
```
      
12345

      
docker run --rm -it --runtime=nvidia \
-v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
-e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
nvcr.io/nvidia-hpcvis/paraview-index:glx-17.11.13-beta \
sh -c paraview\ --server-url=cs://your_server_hostname:11111

    
```

###  [9.4.5. ParaView With NVIDIA OptiX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix)
The ParaView with NVIDIA OptiX container is designed to run ParaView as a user normally would outside a container. The following sections show how to launch the OptiX container with different use cases. 
For more information about ParaView see the [ParaView User’s Guide](https://www.paraview.org/paraview-guide/) and the [NVIDIA OptiX SDK](https://developer.nvidia.com/optix). 
###  [9.4.5.1. Single-Machine Container With GLX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-single)
On systems with a physical display, or when running a ParaView client, users will wish to launch a container with GLX support. This can be done as follows. 
  1. Pull the docker image:
Copy
Copied!
```
      
1

      
docker pull nvcr.io/nvidia-hpcvis/paraview-optix:glx-17.11.13-beta

    
```

  2. Set up X11 forwarding variables:
Copy
Copied!
```
      
      
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth;
touch /tmp/.docker.xauth;
xauth nlist :0 | sed -e 's/^..../ffff/' | xauth -f /tmp/.docker.xauth nmerge -

    
```

  3. Run the image. In this example, host system data in the current directory `$(pwd)` are mounted to both `/work` in the container. This should be modified as desired. 
Copy
Copied!
```
      
      
docker run --rm -it --runtime=nvidia -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 -v $(pwd):/work:rw nvcr.io/nvidia-hpcvis/paraview-optix-glx-beta:17.11.10 sh -c paraview

    
```



###  [9.4.5.2. Server Container With EGL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-server)
Launching a ParaView server on GPU HPC resources often requires EGL support, requiring a separate build of ParaView for which we have a separate container. 
  1. Pull the container:
Copy
Copied!
```
      
      
docker pull nvcr.io/nvidia-hpcvis/paraview-optix:egl-17.11.13-beta

    
```

  2. Specify the connection port and launch the container as follows (in this example, we listen on the default port `11111`): 
Copy
Copied!
```
      
      
docker run --runtime=nvidia -p 11111:11111 --rm -it \
nvcr.io/nvidia-hpcvis/paraview-optix:egl-17.11.13-beta sh -c pvserver

    
```

  3. For users who wish to run the server on a GLX-capable workstation, it is equally possible to use the GLX image with the `pvserver` argument. 


###  [9.4.5.3. Running The GLX Client And Attaching To The Server](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-glx)
With the server launched, it is then straightforward to use the GLX image to run a client, and connect to the server as follows. Here we assume the server is listening on port `11111`, addressable at `your.server.address`. 
Copy
Copied!
```
      
      
docker pull nvcr.io/nvidia-hpcvis/paraview-optix:glx-17.11.13-beta
XSOCK=/tmp/.X11-unix; XAUTH=/tmp/.docker.xauth
touch /tmp/.docker.xauth
xauth nlist :0 | sed -e 's/^..../ffff/' \
| xauth -f /tmp/.docker.xauth nmerge -
docker run --rm -it --runtime=nvidia \
-v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
-e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
nvcr.io/nvidia-hpcvis/paraview-optix:glx-17.11.13-beta \
sh -c paraview\ --server-url=cs://your.server.address:11111

    
```

###  [9.4.5.4. Optional: Using The ParaView .config File](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-config)
It is helpful to reuse ParaView configuration files to maintain settings across ParaView sessions. To do this, first create a new directory for ParaView to store its settings. 
Copy
Copied!
```
      
      
mkdir pvsettings

    
```

When issuing the `docker run` command, add the following command as an argument: 
Copy
Copied!
```
      
      
-v $(pwd)/pvsettings:/home/paraview/.config/ParaView

    
```

Insert the command before the image URL. For example, 
Copy
Copied!
```
      
      
docker run --rm -it --runtime=nvidia \
 -v /tmp/.X11-unix:/tmp/.X11-unix -v /tmp/.docker.xauth:/tmp/.docker.xauth \
 -e XAUTHORITY=/tmp/.docker.xauth -e DISPLAY=:0 \
 nvcr.io/nvidia-hpcvis/paraview-optix:glx-17.11.13-beta \
 -v $(pwd)/pvsettings:/home/paraview/.config/ParaView \
 sh -c paraview\ --server-url=cs://your.server.address:11111

    
```

## [10. Pulling NGC Containers from NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pullcontainer)
Before you using a container from the NGC Catalog, review the prerequisites described in the [Prerequisites](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-image-prerequisites) section. 
To become a registered NGC user, follow the steps explained in the [Registering and Activating a New NGC Org to Obtain Authenticated Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#registering-activating-ngc-account "Instructions for registering and activating a new NGC org."). 
###  [10.1. Key NGC Container Registry Terminology](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#keyconcepts)
In order to issue the pull and run commands, ensure that you are familiar with the following concepts. A pull command looks similar to: 
Copy
Copied!
```
      
1

      
docker pull nvcr.io/nvidia/caffe2:17.10

    
```

A run command looks similar to: 
Copy
Copied!
```
      
1

      
docker run --gpus all -it --rm –v local_dir:container_dir nvcr.io/nvidia/caffe2:<xx.xx>

    
```

Note:
The base command `docker run --gpu all` assumes that your system has Docker 19.03-CE installed. See the section [Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support) for the command to use for earlier versions of Docker. 
The following concepts describe the separate attributes that make up the both commands.  

`nvcr.io` 
     The name of the container registry, which for the NGC container registry is `nvcr.io`.  

`nvidia` 
     The name of the space within the registry that contains the container. For containers provided by NVIDIA, the registry space is `nvidia`. For more information, see [NGC Container Images in NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-catalog-containers).  

`-it` 
     You want to run the container in interactive mode.  

`--rm` 
     You want to delete the container when finished.  

`–v` 
     You want to mount the directory.  

`local_dir` 
     The directory or file from your host system (absolute path) that you want to access from inside your container. For example, the `local_dir` in the following path is `/home/jsmith/data/mnist`. 
Copy
Copied!
```
      
      
-v /home/jsmith/data/mnist:/data/mnist

    
```

If you are inside the container, for example, using the command `ls /data/mnist`, you will see the same files as if you issued the ls `/home/jsmith/data/mnist` command from outside the container.  

`container_dir` 
     The target directory when you are inside your container. For example, `/data/mnist` is the target directory in the example: 
Copy
Copied!
```
      
      
-v /home/jsmith/data/mnist:/data/mnist

    
```


`<xx.xx>` 
     The tag. For example, 17.10. 
You can access the NGC container registry by running a Docker commands from any Linux computer with Internet access on which Docker is installed.You can access the NGC container registry at `nvcr.io` through the Docker CLI. 
Before accessing the NGC container registry, see [_NGC Getting Started Guide_](http://docs.nvidia.com/ngc/ngc-getting-started-guide/index.html) for instructions on how to access the website and, if you intend to access locked NGC content, know how to sign up for an NGC account and obtain an API key. 
###  [10.2. Accessing And Pulling an NGC Container Image via the Docker CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#accessing_registry)
###  [10.2.1. Logging in to the NGC container registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#logging-in-to-ngc-registry)
Before accessing locked NGC content, you must sign up for an NGC account and obtain an API key as explained in the section [Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-api-key). Then log in to the NGC registry from the command line as follows. 
  1. Log in to the NGC container registry.
Copy
Copied!
```
      
      
$ docker login nvcr.io

    
```

  2. When prompted for your user name, enter the following text: 
Copy
Copied!
```
      
      
$oauthtoken

    
```

The `$oauthtoken` username is a special user name that indicates that you will authenticate with an API key and not a username and password. 
  3. When prompted for your password, enter your NGC API key as shown in the following example. 
Copy
Copied!
```
      
      
Username: $oauthtoken
Password: k7cqFTUvKKdiwGsPnWnyQFYGnlAlsCIRmlP67Qxa

    
```

Tip:
When you get your API key, copy it to the clipboard so that you can paste the API key into the command shell when you are prompted for your password. 
  4. Confirm "Login Success".


###  [10.2.2. Pulling a Container from NGC Container Registry Using Docker CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pull_ngc_docker)
You can browse the available containers in the NGC container registry by opening the [NGC website](https://ngc.nvidia.com) using a web browser 
  1. Browse the NGC Catalog, select the image to pull, then copy the pull command.
The following image shows the pull comand on the PyTorch container page.
![pytorch-page.png](https://docscontent.nvidia.com/dims4/default/2d4526a/2147483647/strip/true/crop/1152x993+0+0/resize/1152x993!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fpytorch-page.png)
  2. Click the download icon to copy the pull command to the clipboard.
  3. Log in to nvcr.io, then paste the command in your terminal. For example, to pull the PyTorch container: 
Copy
Copied!
```
      
      
$ docker pull nvcr.io/nvidia/pytorch:20.03-py3

    
```

See the [NGC Getting Started Guide](https://docs.nvidia.com/ngc/ngc-getting-started-guide/index.html) for details on using the NGC website. 
  4. List the Docker images on your system to confirm that the container was pulled. 
Copy
Copied!
```
      
      
$ docker images

    
```

For more information pertaining to your specific container, refer to the `/workspace/README.md` file inside the container. 


After pulling a container, you can run jobs in the container to run scientific workloads, train neural networks, deploy deep learning models, or perform AI analytics. 
###  [Accessing and Pulling an NGC Catalog Container Using NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#access-container-via-ngc-cli)
If you will be pulling containers from the registry, you will need Docker installed on your local machine. To install Docker on your client machine, follow one of these instructions: 
  * For Ubuntu Linux: 
<https://docs.docker.com/engine/installation/linux/ubuntulinux/>
  * For Windows: 
<https://docs.docker.com/engine/installation/windows/#/docker-for-windows>
  * For MacOS X: 
<https://docs.docker.com/engine/installation/mac/>


This document provides an introduction to using the NGC Catalog CLI. For a complete list of commands and options, use the `-h` option as explained in [index.html#getting-help](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#getting-help). 
###  [10.3.1. Viewing Container Image Information](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#viewing-container-image)
There are several commands for viewing information about available container images. 
**To list container images:**
Copy
Copied!
```
      
      
C:\>ngc registry image list

    
```

Example output 
Copy Copied! ```
      
      +-----------+----------------+------------+------------+--------------+------------+
| Name   | Repository   | Latest Tag | Image Size | Updated Date | Permission |
+-----------+----------------+------------+------------+--------------+------------+
| BigDFTZ  | hpv/bigdftfe  | cuda10-ubun| 2.37 GB  | Oct 18, 2019 | unlocked  |
|      |        | tu1804-ompi|      | 2019     |      |
| CANDLE  | hpc/candle   | 201803263 | 1.52 GB  | Oct 18, 2019 | unlocked  |
 ...|
    
```
  
---  
**To view detailed information about a specific image, specify the image and the tag.**
**Example** : 
Copy Copied! ```
      
      C:\>ngc registry image info nvidia/caffe:19.02-py2
--------------------------------------------------
 Image Information
 Name: nvidia/caffe:19.02-py2
 Architecture: amd64
 Schema Version: 1
--------------------------------------------------
    
```
  
---  
###  [Pulling a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pushing-container)
With the NGC Registry CLI you can pull (download) images to your system. 
**To pull an image to your registry space, specify the image and, optionally, the tag.**
Copy
Copied!
```
      
      
C:\>ngc registry image pull <image-name>[:<tag>]

    
```

If a tag is not specified, then the tag '`latest`' will be used. 
Note:
nvcr.io/nvidia, nvcr.io/partners and nvcr.io/hpc is reserved namespace and does not grant permissions to users to push or delete container images, models, helm and all artifacts. 
## [11. NGC Container Image Versions](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvdocimver)
Each release of an NGC image is identified by a version "tag". For simpler images this version tag usually contains the version of the major software package in the image. More complex images which contain multiple software packages or versions may use a separate version solely representing the containerized software configuration. One common scheme is versioning by the year and month of the image release. **For example, the 20.01 release of an image was released in January, 2020.**
An image name consists of two parts separated by a colon. The first part is the name of the container in the repository and the second part is the "tag" associated with the container. These two pieces of information are shown in Figure 2, which is the output from issuing the docker images command. 
_Figure 1. Output from`docker images` command_
![image_versions.png](https://docscontent.nvidia.com/dims4/default/f369851/2147483647/strip/true/crop/706x134+0+0/resize/706x134!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fimage_versions.png)
Figure 2 shows simple examples of image names, such as: 
  * `nvidia-cuda:8.0-devel`
  * `ubuntu:latest`
  * `nvcr.io/nvidia/tensorflow:17.01`


If you choose not to add a tag to an image, by default the word "latest" is added as the tag, however all NGC containers have an explicit version tag. 
In the next sections, you will use these image names for running containers. Later in the document, there is also a section on creating your own containers or customizing and extending existing containers. 
## [12. NVIDIA Signed Container Images in NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-container-signatures)
Software signing is the standard mechanism for establishing trust when distributing software, determining which software to trust, and allowing for execution. 
Container image signing adds a digital signature to an image. This signature allows users to validate where an image came from and verify the image was not tampered with. 
Starting in July 2023, all NVIDIA container images published on the NGC Catalog will be signed. 
###  [12.1. Checking for Signed Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images)
There are two ways to determine which containers are signed. 
###  [12.1.1. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images-ui)
Click on **Catalog > Containers** from the left navigation menu. Expand the **Signed Images** filter to the left and select **Yes**. The container images tagged with **Signed Images** will display. 
![ngc-catalog-containers-signed-ann-1280x905.png](https://docscontent.nvidia.com/dims4/default/9c88d14/2147483647/strip/true/crop/1663x947+0+0/resize/1440x820!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-signed-ann-1280x905.png)
Select a container image to view the details. On the details page, you will see the **Signed Images** badge on the left panel and the **Signed** badge on the pane in the **Tags** tab. 
![ngc-catalog-containers-signed-details-ann-1280x666.png](https://docscontent.nvidia.com/dims4/default/06a81b7/2147483647/strip/true/crop/1156x874+0+0/resize/1156x874!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-signed-details-ann-1280x666.png)
###  [12.1.2. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images-cli)
To find signed container images using the CLI, issue the following: 
Copy
Copied!
```
      
      
$ ngc registry image list <image_name>

    
```

**Example** : List all images with name containing 'nginx' 
Copy
Copied!
```
      
      
$ ngc registry image list '*nginx*'

    
```

![ngc-catalog-containers-signed-cli-980x396.png](https://docscontent.nvidia.com/dims4/default/c74f071/2147483647/strip/true/crop/980x396+0+0/resize/980x396!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-signed-cli-980x396.png)
If the image is signed, you can see a value populated in the **Latest Tag** column. 
###  [12.2. Finding NVIDIA's Public Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key)
The public key associated with the signed image can be used to validate its authenticity. You can find the public key of the container in the following ways. 
###  [12.2.1. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key-ui)
On the container details page, select the **Tags** tab. Click on "View all public keys" in the banner. 
![ngc-catalog-containers-signed-details-view-public-ann-1280x666.png](https://docscontent.nvidia.com/dims4/default/4139f49/2147483647/strip/true/crop/1142x478+0+0/resize/1142x478!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-signed-details-view-public-ann-1280x666.png)
The public key URL will display in the dialog. 
![ngc-catalog-containers-view-all-public-rounded.png](https://docscontent.nvidia.com/dims4/default/ea3ecd9/2147483647/strip/true/crop/1155x586+0+0/resize/1155x586!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-view-all-public-rounded.png)
###  [12.2.2. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key-cli)
To find NVIDIA’s public key using the CLI, issue the following command: 
![ngc-public-key-643x174.png](https://docscontent.nvidia.com/dims4/default/e60783c/2147483647/strip/true/crop/643x174+0+0/resize/643x174!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-public-key-643x174.png)
###  [12.3. Verifying NVIDIA's Signature](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#verifying-nv-signature)
The following tools are examples that you can use to verify the signature. There are also other tools available. 
###  [Using Cosign](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#using-cosign)
Cosign is a tool for signing container images. To begin, follow the installation instructions provided at the URL below to set up Cosign: 
[_https://docs.sigstore.dev/cosign/installation/_](https://docs.sigstore.dev/cosign/installation/)
Once Cosign is set up, issue the following command to verify the signature of the container image: 
Copy
Copied!
```
      
      
$ cosign verify [--key <key path>|<key url>|<kms uri>] <image uri>

    
```

Make sure to replace the placeholders within the square brackets with the appropriate values: 
  * `<key path>`: Path to the key file (if using a local key). 
  * `<key URL>`: URL pointing to the key file (if using a remote key). 
  * `<KMS URI>`: URI for the Key Management Service (if using a KMS for key management). 
  * `<image URI>`: URI of the container image you wish to verify. 


Cosign 2.x releases introduced a new flag `--insecure-ignore-tlog=true` for key-based signing with the `cosign verify` command. Please include this flag when using Cosign 2.x versions. Prior to version 2.x, this flag is not required as it is set as the default behavior. 
Copy
Copied!
```
      
      
cosign verify --insecure-ignore-tlog [--key <key path>|<key url>|<kms uri>] <image uri>

    
```

###  [12.3.2. Using an Admission Controller in Kubernetes Clusters](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#verifying-nv-signature-admission-controller)
Several Open Source Software (OSS) admission controllers offer the capability of sigstore-based image verification. These powerful tools allow you to verify the integrity and authenticity of containers deployed within your Kubernetes environment. 
For example, Connaisseur is a Kubernetes admission controller that can be used to integrate container image signature verification and trust pinning into a cluster. It ensures that only signed images are allowed to run in a cluster. 
To set up Connaisseur, follow the steps outlined in the documentation below: 
  * [_Getting started Guide_](https://sse-secure-systems.github.io/connaisseur/v2.8.0/getting_started/)
  * [_Cosign Validator setup_](https://sse-secure-systems.github.io/connaisseur/v2.8.0/validators/sigstore_cosign/)
  * [_Test Connaisseur_](https://sse-secure-systems.github.io/connaisseur/v2.8.0/getting_started/#test-connaisseur)


After configuring the Connaisseur validator, you can test it by running a container in the Kubernetes (K8s) cluster using the following command for a signed image: 
Copy
Copied!
```
      
      
kubectl run test --image=${IMAGE}

    
```

When you run the container with the command, the request is admitted to the cluster if the image is signed and passes the verification. Kubernetes will return the following response: 
Copy
Copied!
```
      
      
pod/test created

    
```

## [13. Running an NGC Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#runcont)
Before you can run an NGC deep learning framework container, your Docker environment must support NVIDIA GPUs. To run a container, issue the appropriate command as explained in this chapter, specifying the registry, repository, and tags. 
###  [13.1. Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support)
To obtain the best performance when running NGC containers, three methods of providing GPU support for Docker containers have been developed: 
  * Native GPU support (included with Docker-ce 19.03 or later)
  * NVIDIA Container Runtime for Docker (`nvidia-docker2` package) 
  * Docker Engine Utility for NVIDIA GPUs (`nvidia-docker` package) 


The method implemented in your system depends on the DGX OS version installed (for DGX systems), the specific NGC Cloud Image provided by a Cloud Service Provider, or the software that you have installed in preparation for running NGC containers on TITAN PCs, Quadro PCs, or vGPUs. 
Refer to the following table to assist in determining which method is implemented in your system. 
**GPU Support Method**| **When Used**| **How to Determine**  
---|---|---  
Native GPU Support| Included with Docker-ce 19.03 or later| Run `docker version` to determine the installed Docker version.   
NVIDIA Container Runtime for Docker| If the nvidia-docker2 package is installed| Run `nvidia-docker version` and check for NVIDIA Docker version 2.0 or later   
Docker Engine Utility for NVIDIA GPUs| If the nvidia-docker package is installed| Run `nvidia-docker version`and check for NVIDIA Docker version 1.x   
Each method is invoked by using specific Docker commands, described as follows. 
**Using Native GPU support**
Note:
If Docker is updated to 19.03 on a system which already has nvidia-docker or nvidia-docker2 installed, then the corresponding methods can still be used. 
  * To use the native support on a new installation of Docker, first enable the new GPU support in Docker. 
Copy
Copied!
```
      
      
$ sudo apt-get install -y docker nvidia-container-toolkit

    
```

This step is not needed if you have updated Docker to 19.03 on a system with nvidia-docker2 installed. The native support will be enabled automatically. 
  * Use docker run --gpus to run GPU-enabled containers.
    * Example using all GPUs
Copy
Copied!
```
      
      
$ sudo docker run --gpus all ...

    
```

    * Example using two GPUs
Copy
Copied!
```
      
      
$ sudo docker run --gpus 2 ...

    
```

    * Examples using specific GPUs
Copy
Copied!
```
      
      
$ sudo docker run --gpus "device=1,2" ...

    
```

Copy
Copied!
```
      
      
$ sudo docker run --gpus "device=UUID-ABCDEF,1" ...

    
```



**Using the NVIDIA Container Runtime for Docker**
With the NVIDIA Container Runtime for Docker installed (nvidia-docker2), you can run GPU-accelerated containers in one of the following ways. 
  * Use docker run and specify runtime=nvidia.
Copy
Copied!
```
      
      
$ sudo docker run --runtime=nvidia ...

    
```

  * Use nvidia-docker run.
Copy
Copied!
```
      
      
$ sudo nvidia-docker run ...

    
```

The new package provides backward compatibility, so you can still run GPU-accelerated containers by using this command, and the new runtime will be used. 


Use docker run with nvidia as the default runtime. 
You can set nvidia as the default runtime, for example, by adding the following line to the /etc/docker/daemon.json configuration file as the first entry. 
Copy
Copied!
```
      
      
"default-runtime": "nvidia",

    
```

The following is an example of how the added line appears in the JSON file. Do not remove any pre-existing content when making this change. 
Copy
Copied!
```
      
      
{
 "default-runtime": "nvidia",
 "runtimes": {
   "nvidia": {
     "path": "/usr/bin/nvidia-container-runtime",
     "runtimeArgs": []
   }
 },
}

    
```

You can then use docker run to run GPU-accelerated containers. 
Copy
Copied!
```
      
      
$ sudo docker run ...

    
```

CAUTION:
If you build Docker images while `nvidia` is set as the default runtime, make sure the build scripts executed by the Dockerfile specify the GPU architectures that the container will need. Failure to do so may result in the container being optimized only for the GPU architecture on which it was built. Instructions for specifying the GPU architecture depend on the application and are beyond the scope of this document. Consult the specific application build process for guidance. 
**Using the Docker Engine Utility for NVIDIA GPUs**
With the Docker Engine Utility for NVIDIA GPUs installed (nvidia-docker), run GPU-enabled containers as follows. 
Copy
Copied!
```
      
      
$ sudo nvidia-docker run ...

    
```

###  [13.2. Running NGC Containers with Runtime Resources ](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvdocrun)
On a system with GPU support for NGC containers, the following occurs when running a container. 
  * The Docker Engine loads the image into a container which runs the software. 
  * You define the runtime resources of the container by including additional flags and settings that are used with the command. These flags and settings are described in the following sections. 
  * The GPUs are explicitly defined for the Docker container (defaults to all GPUs, can be specified using _NV_GPU_ environment variable). 


Note:
The base command `docker run --gpu all` assumes that your system has Docker 19.03-CE installed. See the section [Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support) for the command to use for earlier versions of Docker. 
  1. As a user, run the container interactively.
Copy
Copied!
```
      
      
$ docker run --gpus all -it --rm –v local_dir:container_dir
     nvcr.io/nvidia/<repository>:<xx.xx>

    
```

The following example runs the December 2016 release (16.12) of the NVCaffe container in interactive mode. The container is automatically removed when the user exits the container. 
Copy
Copied!
```
      
      
$ docker run --gpus all --rm -ti nvcr.io/nvidia/caffe:16.12
===========
== Caffe ==
===========
NVIDIA Release 16.12 (build 6217)
Container image Copyright (c) 2016, NVIDIA CORPORATION. All rights reserved.
Copyright (c) 2014, 2015, The Regents of the University of California (Regents)
All rights reserved.
Various files include modifications (c) NVIDIA CORPORATION. All rights reserved.
NVIDIA modifications are covered by the license terms that apply to the underlying project or file.
root@df57eb8e0100:/workspace#

    
```

  2. From within the container, start the job that you want to run. The precise command to run depends on the deep learning framework in the container that you are running and the job that you want to run. For details see the `/workspace/README.md` file for the container. 
The following example runs the `caffe time` command on one GPU to measure the execution time of the `deploy.prototxt` model. 
Copy
Copied!
```
      
      
# caffe time -model models/bvlc_alexnet/ -solver deploy.prototxt -gpu=0

    
```

  3. **Optional:** Run the December 2016 release (16.12) of the same NVCaffe container but in non-interactive mode.
Copy
Copied!
```
      
      
% docker run --gpus all --rm nvcr.io/nvidia/caffe:16.12 caffe time -model
   /workspace/models/bvlc_alexnet -solver /workspace/deploy.prototxt -gpu=0

    
```



###  [13.2.1. Specifying A User](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#specifyuser)
Unless otherwise specified, the user inside the container is the root user. When running within the container, files created on the host operating system or network volumes can be accessed by the root user. This is unacceptable for some users and they will want to set the ID of the user in the container. For example, to set the user in the container to be the currently running user, issue the following: 
Copy
Copied!
```
      
      
% docker run --gpus all -ti --rm -u $(id -u):$(id -g) nvcr.io/nvidia/<repository>:<tag>

    
```

Typically, this results in warnings due to the fact that the specified user and group do not exist in the container. You might see a message similar to the following: 
Copy
Copied!
```
      
      
groups: cannot find name for group ID 1000I have no name! @c177b61e5a93:/workspace$

    
```

The warning can usually be ignored. 
###  [13.2.2. Setting The Remove Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setremflag)
By default, Docker containers remain on the system after being run. Repeated pull or run operations use up more and more space on the local disk, even after exiting the container. Therefore, it is important to clean up the nvidia-docker containers after exiting. 
Note:
Do not use the `--rm` flag if you have made changes to the container that you want to save, or if you want to access job logs after the run finishes. 
To automatically remove a container when exiting, add the `--rm` flag to the run command. 
Copy
Copied!
```
      
      
% docker run --gpus all --rm nvcr.io/nvidia/<repository>:<tag>

    
```

###  [13.2.3. Setting The Interactive Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setintflag)
By default, containers run in batch mode; that is, the container is run once and then exited without any user interaction. Containers can also be run in interactive mode as a service. To run in interactive mode, add the `-ti` flag to the run command. 
Copy
Copied!
```
      
      
% docker run --gpus all -ti --rm nvcr.io/nvidia/<repository>:<tag>

    
```

###  [13.2.4. Setting The Volumes Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setvolflag)
There are no data sets included with the containers, therefore, if you want to use data sets, you need to mount volumes into the container from the host operating system. For more information, see [Manage data in containers](https://docs.docker.com/engine/tutorials/dockervolumes/). 
Typically, you would use either Docker volumes or host data volumes. The primary difference between host data volumes and Docker volumes is that Docker volumes are private to Docker and can only be shared amongst Docker containers. Docker volumes are not visible from the host operating system, and Docker manages the data storage. Host data volumes are any directory that is available from the host operating system. This can be your local disk or network volumes.  

Example 1 
     Mount a directory `/raid/imagedata` on the host operating system as `/images` in the container. 
Copy
Copied!
```
      
      
% docker run --gpus all -ti --rm -v /raid/imagedata:/images
    nvcr.io/nvidia/<repository>:<tag>

    
```


Example 2 
     Mount a local docker volume named `data` (must be created if not already present) in the container as `/imagedata`. 
Copy
Copied!
```
      
      
% docker run --gpus all -ti --rm -v data:/imagedata nvcr.io/nvidia/<repository>:<tag>

    
```

###  [13.2.5. Setting The Mapping Ports Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setmapportflag)
Applications such as Deep Learning GPU Training System™ (DIGITS) open a port for communications. You can control whether that port is open only on the local system or is available to other computers on the network outside of the local system. Using DIGITS as an example, in DIGITS 5.0 starting in container image 16.12, by default the DIGITS server is open on port 5000. However, after the container is started, you may not easily know the IP address of that container. To know the IP address of the container, you can choose one of the following ways: 
  * Expose the port using the local system network stack (`--net=host`) where port 5000 of the container is made available as port 5000 of the local system. 


or 
  * Map the port (`-p 8080:5000`) where port 5000 of the container is made available as port 8080 of the local system. 


In either case, users outside the local system have no visibility that DIGITS is running in a container. Without publishing the port, the port is still available from the host, however not from the outside. 
###  [13.2.6. Setting The Shared Memory Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setincshmem)
Certain applications, such as PyTorch™ and the Microsoft® Cognitive Toolkit™ , use shared memory buffers to communicate between processes. Shared memory can also be required by single process applications, such as MXNet™ and TensorFlow™ , which use the NVIDIA® Collective Communications Library ™ (NCCL) (NCCL). 
By default, Docker containers are allotted 64MB of shared memory. This can be insufficient, particularly when using all 8 GPUs. To increase the shared memory limit to a specified size, for example `1GB`, include the `--shm-size=1g` flag in your `docker run` command. 
Alternatively, you can specify the `--ipc=host` flag to re-use the host’s shared memory space inside the container. Though this latter approach has security implications as any data in shared memory buffers could be visible to other containers. 
###  [13.2.7. Setting The Restricting Exposure Of GPUs Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setresgpuflag)
From inside the container, the scripts and software are written to take advantage of all available GPUs. To coordinate the usage of GPUs at a higher level, you can use this flag to restrict the exposure of GPUs from the host to the container. For example, if you only want GPU 0 and GPU 1 to be seen in the container, you would issue the following: 
**Using native GPU support**
Copy
Copied!
```
      
      
$ docker run --gpus "device=0,1" ...

    
```

**Using`nvidia-docker2`**
Copy
Copied!
```
      
      
$ NV_GPU=0,1 docker run --runtime=nvidia ...

    
```

**Using`nvidia-docker`**
Copy
Copied!
```
      
      
$ NV_GPU=0,1 nvidia-docker run ...

    
```

This flag creates a temporary environment variable that restricts which GPUs are used. 
Specified GPUs are defined per container using the Docker device-mapping feature, which is currently based on Linux `cgroups`. 
###  [13.2.8. Container Lifetime](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setstatusoption)
The state of an exited container is preserved indefinitely if you do not pass the `--rm` flag to the `docker run` command. You can list all of the saved exited containers and their size on the disk with the following command: 
Copy
Copied!
```
      
      
$ docker ps --all --size --filter Status=exited

    
```

The container size on the disk depends on the files created during the container execution, therefore the exited containers take only a small amount of disk space. You can permanently remove a exited container by issuing: 
Copy
Copied!
```
      
      
docker rm [CONTAINER ID]

    
```

By saving the state of containers after they have exited, you can still interact with them using the standard Docker commands. For example: 
  * You can examine logs from a past execution by issuing the `docker logs` command. 
Copy
Copied!
```
      
      
$ docker logs 9489d47a054e

    
```

  * You can extract files using the `docker cp` command.
Copy
Copied!
```
      
      
$ docker cp 9489d47a054e:/log.txt .

    
```

  * You can restart a stopped container using the `docker restart` command. 
Copy
Copied!
```
      
      
$ docker restart <container name>

    
```

For the NVCaffe™ container, issue this command: 
Copy
Copied!
```
      
      
$ docker restart caffe

    
```

  * You can save your changes by creating a new image using the `docker commit` command. For more information, see [Example 3: Customizing a Container using ](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockercommit)`docker commit[](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockercommit)`. 
Note:
Use care when committing Docker container changes, as data files created during use of the container will be added to the resulting image. In particular, core dump files and logs can dramatically increase the size of the resulting image. 


## [14. Multi-Architecture Support for NGC Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#multi-arch-support)
The NGC Container Registry allows users to leverage [_docker multi-architecture_](https://docs.docker.com/docker-for-mac/multi-arch/). It can support multiple architectures, which means that a single image may contain variants for different CPU architectures like ARM, x86, IBM POWER and others ; and sometimes for different operating systems, such as Windows. When running an image, docker will automatically select an image variant which matches the target deployment OS and architecture. 
##  [Manifest Lists and Tags](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#multi-arch-support__section_fmf_dmg_kmb)
The NGC Container Registry supports the manifest list schema application/vnd.docker.distribution.manifest.list.v2+json providing the ability to assign multiple tags per image. To inspect the manifest list, please follow the instructions [_here._](https://docs.docker.com/registry/spec/manifest-v2-2/)
NGC UI allows users to easily identify multi-architecture containers and see the supported CPU architectures. 
![ngc-supported-architectures.png](https://docscontent.nvidia.com/dims4/default/33b273b/2147483647/strip/true/crop/1794x494+0+0/resize/1440x397!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-supported-architectures.png)
##  [Basic Docker Commands for Multi-architecture Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#multi-arch-support__section_hmf_dmg_kmb)
**Inspect Manifest : Display an image manifest or manifest list**
`$ docker manifest inspect <container_name>:<tag>`
More help on manifest:[_link_](https://docs.docker.com/engine/reference/commandline/manifest/)
**Pull a specific image for an architecture**
In order to pull an image with a specific architecture, first do docker manifest which lists multiple platforms and then pull with a specific platform name that matches with the manifest digest. 
`$ docker pull --platform=<arch>`
More help on the above docker command: [_link_](https://docs.docker.com/engine/reference/commandline/pull/)
## [15. Customizing Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontfrm)
NGC images come prepackaged, tuned, and ready to run; however, you may want to build a new image from scratch or augment an existing image with custom code, libraries, data, or settings for your corporate infrastructure. This section will guide you through exercises that will highlight how to create a container from scratch, customize a container, extend a deep learning framework to add features, develop some code using that extended framework from the developer environment, then package that code as a versioned release. 
By default, you do not need to build a container. The NGC container registry, `nvcr.io`, has a number of containers that can be used immediately. These include containers for deep learning, scientific computing and visualization, as well as containers with just the CUDA Toolkit. 
One of the great things about containers is that they can be used as starting points for creating new containers. This can be referred to as "customizing" or "extending" a container. You can create a container completely from scratch, however, since these containers are likely to run on a GPU system, it is recommended that you are least start with a `nvcr.io` container that contains the OS and CUDA. However, you are not limited to this and can create a container that runs on the CPUs in the system which does not use the GPUs. In this case, you can start with a bare OS container from Docker. However, to make development easier, you can still start with a container with CUDA - it is just not used when the container is used. 
In the case of the DGX-1 and the DGX Station, you can push or save your modified/extended containers to the NVIDIA DGX container registry, `nvcr.io`. They can also be shared with other users of the DGX system but this requires some administrator help. 
Currently, you cannot save customized containers from the NGC container registry (cloud based) solution to `nvcr.io`. The customized or extended containers can be saved to a user's private container repository. It is important to note that all NGC deep learning framework images include the source to build the framework itself as well as all of the prerequisites. 
Attention:
Do not install an NVIDIA driver into the Docker® image at Docker build time. nvidia-docker is essentially a wrapper around Docker that transparently provisions a container with the necessary components to execute code on the GPU. 
NVIDIA provides a large set of images in the NGC container registry that are already tested, tuned, and are ready to run. You can pull any one of these images to create a container and add software or data of your choosing. 
A best-practice is to avoid `docker commit` usage for developing new docker images, and to use Dockerfiles instead. The Dockerfile method provides visibility and capability to efficiently version-control changes made during development of a docker image. The docker commit method is appropriate for short-lived, disposable images only (see [Example 3: Customizing A Container Using docker commit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockercommit) for an example). 
For more information on writing a Docker file, see the [best practices documentation](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices). 
###  [15.1. Benefits And Limitations To Customizing A Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#benlimcustcont)
You can customize a container to fit your specific needs for numerous reasons; for example, you depend upon specific software that is not included in the container that NVIDIA provides. No matter your reasons, you can customize a container. 
The container images do not contain sample data-sets or sample model definitions unless they are included with the framework source. Be sure to check the container for sample data-sets or models. 
###  [15.2. Example 1: Building A Container From Scratch](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#buildcontscratch)
Docker uses Dockerfiles to create or build a Docker image. Dockerfiles are scripts that contain commands that Docker uses successively to create a new Docker image. Simply put, a Dockerfile is the source code for the container image. Dockerfiles always start with a base image to inherit from. 
For more information, see [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/). 
  1. Create a working directory on your local hard-drive.
  2. In that directory, open a text editor and create a file called `Dockerfile`. Save the file to your working directory.
  3. Open your `Dockerfile` and include the following: 
Copy
Copied!
```
      
      
FROM ubuntu:14.04
RUN apt-get update && apt-get install -y curl
CMD echo "hello from inside a container"

    
```

Where the last line `CMD`, executes the indicated command when creating the container. This is a way to check that the container was built correctly. 
For this example, we are also pulling the container from the Docker repository and not the DGX™ system repository. There will be subsequent examples using the NVIDIA® repository. 
  4. Save and close your `Dockerfile`.
  5. Build the image. Issue the following command to build the image and create a tag. 
Copy
Copied!
```
      
      
$ docker build -t <new_image_name>:<new_tag> .

    
```

Note:
This command was issued in the same directory where the Dockerfile is located. 
The output from the docker build process lists "Steps"; one for each line in the Dockerfile. 
For example, let us name the container `test1` and tag it with `latest`. Also, for illustrative purposes, let us assume our private DGX system repository is called `nvidian_sas`. The command below builds the container. Some of the output is shown below so you know what to expect. 
Copy
Copied!
```
      
      
$ docker build -t test1:latest .
Sending build context to Docker daemon 3.072 kB
Step 1/3 : FROM ubuntu:14.04
14.04: Pulling from library/ubuntu
...
Step 2/3 : RUN apt-get update &amp;&amp; apt-get install -y curl
...
Step 3/3 : CMD echo "hello from inside a container"
 ---> Running in 1f491b9235d8
 ---> 934785072daf
Removing intermediate container 1f491b9235d8
Successfully built 934785072daf

    
```

For information about building your image, see [docker build](https://docs.docker.com/engine/reference/commandline/build/). For information about tagging your image, see [docker tag](https://docs.docker.com/engine/reference/commandline/tag/). 
  6. Verify that the build was successful. You should see a message similar to the following:
Copy
Copied!
```
      
      
Successfully built 934785072daf

    
```

This message indicates that the build was successful. Any other message and the build was not successful. 
Note:
The number, `934785072daf`, is assigned when the image is built and is random. 
  7. Confirm you can view your image by issuing the following command and view your container.
Copy
Copied!
```
      
      
$ docker images
REPOSITORY   TAG      IMAGE ID    CREATED        SIZE
test1      latest     934785072daf  19 minutes ago     222 MB

    
```

The new container is now available to be used. 
Note:
The container is local to this DGX system. If you want to store the container in your private repository, follow the next step. 
  8. Store the container in your private Docker repository by pushing it. 
Note:
This applies if you have a private registry account associated with the DGX system purchased by your organization. 
    1. The first step in pushing it, is to tag it.
Copy
Copied!
```
      
      
$ docker tag test1 nvcr.io/nvidian_sas/test1:latest

    
```

    2. Now that the image has been tagged, you can push it to, for example, a private project on `nvcr.io` named `nvidian_sas`.
Copy
Copied!
```
      
      
$ docker push nvcr.io/nvidian_sas/test1:latest
The push refers to a repository [nvcr.io/nvidian_sas/test1]
…

    
```

    3. Verify that the container appears in the `nvidian_sas` repository. 


###  [15.3. Example 2: Customizing A Container Using Dockerfile](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockerfile)
This example uses a Dockerfile to customize the NVCaffe container in `nvcr.io`. Before customizing the container, you should ensure the NVCaffe 17.03 container has been loaded into the registry using the `docker pull` command before proceeding. 
Copy
Copied!
```
      
      
$ docker pull nvcr.io/nvidia/caffe:17.03

    
```

As mentioned earlier in this document, the Docker containers on `nvcr.io` also provide a sample Dockerfile that explains how to patch a framework and rebuild the Docker image. In the directory `/workspace/docker-examples`, there are two sample Dockerfiles. For this example, we will use the `Dockerfile.customcaffe` file as a template for customizing a container. 
  1. Create a working directory called `my_docker_images` on your local hard drive. 
  2. Open a text editor and create a file called `Dockerfile`. Save the file to your working directory.
  3. Open your `Dockerfile` again and include the following lines in the file:
Copy
Copied!
```
      
      
FROM nvcr.io/nvidia/caffe:17.03
# APPLY CUSTOMER PATCHES TO CAFFE
# Bring in changes from outside container to /tmp
# (assumes my-caffe-modifications.patch is in same directory as
Dockerfile)
#COPY my-caffe-modifications.patch /tmp
# Change working directory to NVCaffe source path
WORKDIR /opt/caffe
# Apply modifications
#RUN patch -p1 < /tmp/my-caffe-modifications.patch
# Note that the default workspace for caffe is /workspace
RUN mkdir build && cd build && \
 cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr/local -DUSE_NCCL=ON
-DUSE_CUDNN=ON -DCUDA_ARCH_NAME=Manual -DCUDA_ARCH_BIN="35 52 60 61"
-DCUDA_ARCH_PTX="61" .. && \
 make -j"$(nproc)" install && \
 make clean && \
 cd .. && rm -rf build
# Reset default working directory
WORKDIR /workspace

    
```

Save the file. 
  4. Build the image using the `docker build` command and specify the repository name and tag. In the following example, the repository name is _corp/caffe_ and the tag is _17.03.1PlusChanges_. For the case, the command would be the following: 
Copy
Copied!
```
      
      
$ docker build -t corp/caffe:17.03.1PlusChanges .

    
```

  5. Run the Docker image using the command appropriate to the methoid of GPU support installed. 
Copy
Copied!
```
      
      
$ docker run --gpus all -ti --rm corp/caffe:17.03.1PlusChanges .

    
```

Note:
The base command `docker run --gpu all` assumes that your system has Docker 19.03-CE installed. See the section [Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support) for the command to use for earlier versions of Docker. 


###  [15.4. Example 3: Customizing A Container Using docker commit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockercommit)
This example uses the docker commit command to flush the current state of the container to a Docker image. This is not a recommended best practice, however, this is useful when you have a container running to which you have made changes and want to save them. In this example, we are using the `apt-get` tag to install packages which requires that the user run as root. 
Note:
  * The NVCaffe image release 17.04 is used in the example instructions for illustrative purposes. 
  * Do not use the `--rm` flag when running the container. If you use the `--rm` flag when running the container, your changes will be lost when exiting the container. 


  1. Pull the Docker container from the `nvcr.io` repository to the DGX system. For example, the following command will pull the NVCaffe container:
Copy
Copied!
```
      
      
$ docker pull nvcr.io/nvidia/caffe:17.04

    
```

  2. Run the container on the DGX system. 
Copy
Copied!
```
      
      
$ docker run --gpus all -ti nvcr.io/nvidia/caffe:17.04

    
```

Copy
Copied!
```
      
      
==================
== NVIDIA Caffe ==
==================
NVIDIA Release 17.04 (build 26740)
Container image Copyright (c) 2017, NVIDIA CORPORATION. All rights reserved.
Copyright (c) 2014, 2015, The Regents of the University of California (Regents)
All rights reserved.
Various files include modifications (c) NVIDIA CORPORATION. All rights reserved.
NVIDIA modifications are covered by the license terms that apply to the underlying project or file.
NOTE: The SHMEM allocation limit is set to the default of 64MB. This may be insufficient for NVIDIA Caffe. NVIDIA recommends the use of the following flags:
  nvidia-docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 ...
root@1fe228556a97:/workspace#

    
```

Note:
The base command `docker run --gpu all` assumes that your system has Docker 19.03-CE installed. See the section [Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support) for the command to use for earlier versions of Docker. 
  3. You should now be the root user in the container (notice the prompt). You can use the command `apt` to pull down a package and put it in the container. 
Note:
The NVIDIA containers are built using Ubuntu which uses the `apt-get` package manager. Check the container release notes [Deep Learning Documentation](http://docs.nvidia.com/deeplearning/dgx/) for details on the specific container you are using. 
In this example, we will install Octave; the GNU clone of MATLAB, into the container. 
Copy
Copied!
```
      
      
# apt-get update
# apt install octave

    
```

Note:
You have to first issue `apt-get update` before you install Octave using `apt`. 
  4. Exit the workspace.
Copy
Copied!
```
      
      
# exit

    
```

  5. Display the list of containers using `docker ps -a`. As an example, here is some of the output from the `docker ps -a` command:
Copy
Copied!
```
      
      
$ docker ps -a
CONTAINER ID  IMAGE            CREATED    ...
1fe228556a97  nvcr.io/nvidia/caffe:17.04  3 minutes ago ...

    
```

  6. Now you can create a new image from the container that is running where you have installed Octave. You can commit the container with the following command.
Copy
Copied!
```
      
      
$ docker commit 1fe228556a97 nvcr.io/nvidian_sas/caffe_octave:17.04
sha256:0248470f46e22af7e6cd90b65fdee6b4c6362d08779a0bc84f45de53a6ce9294

    
```

  7. Display the list of images.
Copy
Copied!
```
      
      
$ docker images
REPOSITORY         	TAG       	IMAGE ID   ...
nvidian_sas/caffe_octave  	17.04      	75211f8ec225 ...

    
```

  8. To verify, let's run the container again and see if Octave is actually there. 
Note:
This only works for the DGX-1 and the DGX Station. 
Copy
Copied!
```
      
      
$ docker run --gpus all -ti nvidian_sas/caffe_octave:17.04

    
```

Copy
Copied!
```
      
      
==================
== NVIDIA Caffe ==
==================
NVIDIA Release 17.04 (build 26740)
Container image Copyright (c) 2017, NVIDIA CORPORATION. All rights reserved. Copyright (c) 2014, 2015, The Regents of the University of California (Regents) All rights reserved.
Various files include modifications (c) NVIDIA CORPORATION. All rights reserved. NVIDIA modifications are covered by the license terms that apply to the underlying project or file.
NOTE: The SHMEM allocation limit is set to the default of 64MB. This may be insufficient for NVIDIA Caffe. NVIDIA recommends the use of the following flags:
  nvidia-docker run --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 ...
root@2fc3608ad9d8:/workspace# octave
octave: X11 DISPLAY environment variable not set
octave: disabling GUI features
GNU Octave, version 4.0.0
Copyright (C) 2015 John W. Eaton and others.
This is free software; see the source code for copying conditions.
There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. For details, type 'warranty'.
Octave was configured for "x86_64-pc-linux-gnu".
Additional information about Octave is available at http://www.octave.org.
Please contribute if you find this software useful.
For more information, visit http://www.octave.org/get-involved.html
Read http://www.octave.org/bugs.html to learn how to submit bug reports.
For information about changes from previous versions, type 'news'.
octave:1>

    
```

Since the Octave prompt displayed, Octave is installed.
  9. If you want to save the container into your private repository (Docker uses the phrase "push"), then you can use the command `docker push ...`.
Copy
Copied!
```
      
      
$ docker push nvcr.io/nvidian_sas/caffe_octave:17.04

    
```



The new Docker image is now available for use. You can check your local Docker repository for it. 
###  [15.5. Example 4: Developing A Container Using Docker](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#extendingcont)
There are two primary use cases for a developer to extend a container: 
  1. Create a development image that contains all of the immutable dependencies for the project, but not the source code itself. 
  2. Create a production or testing image that contains a fixed version of the source and all of the software dependencies. 


The datasets are not packaged in the container image. Ideally, the container image is designed to expect volume mounts for datasets and results. 
In these examples, we mount our local dataset from `/raid/datasets` on our host to `/dataset` as a read-only volume inside the container. We also mount a job specific directory to capture the output from a current run. 
In these examples, we will create a timestamped output directory on each container launch and map that into the container at `/output`. Using this method, the output for each successive container launch is captured and isolated. 
Including the source into a container for developing and iterating on a model has many awkward challenges that can over complicate the entire workflow. For instance, if your source code is in the container, then your editor, version control software, dotfiles, etc. also need to be in the container. 
However, if you create a development image that contains everything you need to run your source code, you can map your source code into the container to make use of your host workstation’s developer environment. For sharing a fixed version of a model, it is best to package a versioned copy of the source code and trained weights with the development environment. 
As an example, we will work though a development and delivery example for the open source implementation of the work found in [Image-to-Image Translation with Conditional Adversarial Networks](https://arxiv.org/abs/1611.07004) by Isola et. al. and is available at [pix2pix](https://github.com/phillipi/pix2pix). Pix2Pix is a Torch implementation for learning a mapping from input images to output images using a Conditional Adversarial Network. Since online projects can change over time, we will focus our attention on the snapshot version `d7e7b8b557229e75140cbe42b7f5dbf85a67d097` change-set. In this section, we are using the container as a virtual environment, in that the container has all the programs and libraries needed for our project. 
Note:
We have kept the network definition and training script separate from the container image. This is a useful model for iterative development because the files that are actively being worked on are persistent on the host and only mapped into the container at runtime. 
The differences to the original project can be found here [Comparing changes](https://github.com/ryanolson/pix2pix/compare/master...ryanolson:devel). 
If the machine you are developing on is not the same machine on which you will be running long training sessions, then you may want to package your current development state in the container. 
  1. Create a working directory on your local hard-drive.
Copy
Copied!
```
      
      
mkdir Projects
$ cd ~/Projects

    
```

  2. Git clone the Pix2Pix git repository.
Copy
Copied!
```
      
      
$ git clone https://github.com/phillipi/pix2pix.git
$ cd pix2pix

    
```

  3. Run the git checkout command. 
Copy
Copied!
```
      
      
$ git checkout -b devel d7e7b8b557229e75140cbe42b7f5dbf85a67d097

    
```

  4. Download the dataset:
Copy
Copied!
```
      
      
bash ./datasets/download_dataset.sh facades
I want to put the dataset on my fast /raid storage.
$ mkdir -p /raid/datasets
$ mv ./datasets/facades /raid/datasets

    
```

  5. Create a file called `Dockerfile`, and add the following lines:
Copy
Copied!
```
      
      
FROM nvcr.io/nvidia/torch:17.03
RUN luarocks install nngraph
RUN luarocks install 
https://raw.githubusercontent.com/szym/display/master/display-scm-0.rockspec
WORKDIR /source

    
```

  6. Build the development Docker container image (`build-devel.sh`).
Copy
Copied!
```
      
      
docker build -t nv/pix2pix-torch:devel .

    
```

  7. Create the following `train.sh` script:
Copy
Copied!
```
      
      
#!/bin/bash -x
ROOT="${ROOT:-/source}"
DATASET="${DATASET:-facades}"
DATA_ROOT="${DATA_ROOT:-/datasets/$DATASET}"
DATA_ROOT=$DATA_ROOT name="${DATASET}_generation"
which_direction=BtoA th train.lua

    
```

If you were actually developing this model, you would be iterating by making changes to the files on the host and running the training script which executes inside the container. 
  8. **Optional:** Edit the files and execute the next step after each change. 
  9. Run the training script (`run-devel.sh`).
Copy
Copied!
```
      
      
docker run --gpus all --rm -ti -v $PWD:/source -v
/raid/datasets:/datasets nv/pix2pix-torch:devel ./train.sh

    
```

Note:
The base command `docker run --gpu all` assumes that your system has Docker 19.03-CE installed. See the section [Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support) for the command to use for earlier versions of Docker. 


###  [Example 4.1: Package The Source Into The Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#unique_1584239657)
Packaging the model definition and script into the container is very simple. We simply add a `COPY` step to the Dockerfile. 
We’ve updated the run script to simply drop the volume mounting and use the source packaged in the container. The packaged container is now much more portable than our `devel` container image because the internal code is fixed. It would be good practice to version control this container image with a specific tag and store it in a container registry. 
The updates to run the container are equally subtle. We simply drop the volume mounting of our local source into the container. 
## [16. Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-models)
A discussion of NGC models and how to download them from the NGC Catalog. 
###  [16.1. What are Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#models-what-are)
Many AI applications have common needs: classification, object detection, language translation, text-to-speech, recommender engines, sentiment analysis, and more. When developing applications with these capabilities, it is much faster to start with a model that is pre-trained and then tune it for a specific use case. 
NGC offers pre-trained models for a large number of AI tasks that are optimized for NVIDIA Tensor Core GPUs, and can be easily re-trained by updating just a few layers, saving valuable time. 
So whether you’re looking for content you can simply retrain for your specific use case or a complete model you can grab and deploy right away, NGC has you covered. 
###  [16.2. Searching and Filtering Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-models)
To view NGC models, navigate to **Catalog** > **Models** in the left menu. Use the search bar at the top of the page to filter the types of models or sort the list using the criteria from the dropdown menu. You can refine your search by utilizing the filters under Use Case, NVIDIA Platform, NVIDIA AI Enterprise, and many others. The descriptions for the filtering options are as follows: 
  * **Use Case** : Choose from the available common use cases. 
  * **NVIDIA AI Enterprise Support** : Select this option to find publicly available models supported by NVIDIA AI Enterprise. 
  * **NVIDIA Platform** : Choose from Clara, DeepStream, TensorFlow, and many others. 
  * **NVIDIA AI Enterprise Exclusive** : Choose products under this to see entitled entities. 
  * **Framework** : Filter by framework such as TAO Toolkit, PyTorch, and Riva. 
  * **Industry** : Select by available industries. 
  * **Solution** : Select the solution that closely matches your use case. 
  * **Publisher** : Filter by publisher. 
  * **Language** : Select by language. 
  * **Other** : Miscellaneous options. 


The following example page shows the available models when searching on 'deep learning': 
![ngc-catalog-containers-models-dl-guest-ann.png](https://docscontent.nvidia.com/dims4/default/a9d6b2e/2147483647/strip/true/crop/1301x943+0+0/resize/1301x943!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-models-dl-guest-ann.png)
The filters will contain the results for the matching search criteria or "No results found" if there aren't any matches. 
###  [16.3. Downloading Models via NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-ngc-cli)
A discussion of NGC models and how to download them from the NGC Catalog. 
To download a model from the registry to your local disk, specify the model name and version. 
Copy
Copied!
```
      
      
$ ngc registry model download-version <_org-name_>/<_model-name:version_>

    
```

**Example**
Copy
Copied!
```
      
      
$ ngc registry model download-version nvidia/ngcdocsmodel:1

    
```

The following is an example showing the output confirming completion of the download: 
Copy
Copied!
```
      
      
Downloaded 230.92 MB in 38s, Download speed: 6.07 MB/s
----------------------------------------------------
Transfer id: trt_onnx_vgg16_v100_16g_int8_v1 Download status: Completed.
Downloaded local path: C:\ngcdocsmodel
Total files downloaded: 3
Total downloaded size: 230.92 MB
Started at: 2019-03-18 14:09:31.664000
Completed at: 2019-03-18 14:10:09.712000
Duration taken: 38s seconds
----------------------------------------------------

    
```

The model is downloaded to a folder that corresponds to the model name in the current directory. You can specify another path using the `-d .` option. 
**Example** : Downloading a model to a specific directory (/models). 
Copy
Copied!
```
      
      
$ ngc registry model download-version nvidia/ngcdocsmodel:1 -d ./models

    
```

Copy
Copied!
```
      
      
Downloaded 230.92 MB in 38s, Download speed: 6.07 MB/s
----------------------------------------------------
Transfer id: trt_onnx_vgg16_v100_16g_int8_v1 Download status: Completed.
Downloaded local path: C:\ngcdocsmodel
Total files downloaded: 3
Total downloaded size: 230.92 MB
Started at: 2019-03-18 14:09:31.664000
Completed at: 2019-03-18 14:10:09.712000
Duration taken: 38s seconds
----------------------------------------------------

    
```

###  [16.4. Downloading Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-wget)
###  [16.4.1. Downloading Guest Access Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-guest-access-models-via-wget)
How to download guest access models via WGET/cURL. 
To get a copy of a single file from an NGC Model via wget/curl you can use the URL provided in the NGC UI. 
  1. Open the NGC UI, click **Models** from the left navigation menu and then locate and click the model you want to download. 
![ngc-wget-models.png](https://docscontent.nvidia.com/dims4/default/b261061/2147483647/strip/true/crop/1634x947+0+0/resize/1440x835!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-models.png)
  2. Click the **Download** button on the top right or navigate to the **File Browser** tab. 
![ngc-wget-download.png](https://docscontent.nvidia.com/dims4/default/84108b9/2147483647/strip/true/crop/1211x571+0+0/resize/1211x571!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-download.png)
  3. Select the **Copy curl cmd** or **Copy wget cmd** to copy the relevant code to the clipboard.
![ngc-wget-copy-curl-cmd.png](https://docscontent.nvidia.com/dims4/default/0e69dbc/2147483647/strip/true/crop/1092x530+0+0/resize/1092x530!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-copy-curl-cmd.png)


The following will then be added to your clipboard: `$ wget https://api.ngc.nvidia.com/v2/models/nvidia/<model-name>/versions/<version>/files/<filename>`
###  [16.4.2. Downloading Authenticated Access Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-wget-authenticated-access)
How to download authenticated access models via WGET/cURL. 
  1. Obtain an NGC API Key. See [NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-api-keys). This will be referred to as <_API-key_ > below.
  2. Find orgs and teams scope and model name, model version.
In the example below the <_org_ > is **nvidia** and <_team_ > is **riva** , <_model-name_ > is **speechtotext_en_us_conformer_xl** , <_version_ > is **deployable_v4.0_export_v2** , <_file-name_ > is **Conformer-CTC-XL_spe-128_en-US_Riva-ASR-SET-4.0.riva**
![ngc-catalog-download-auth-access-models.png](https://docscontent.nvidia.com/dims4/default/cb089a5/2147483647/strip/true/crop/1453x551+0+0/resize/1440x546!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-download-auth-access-models.png)
**Note:** Not all models are within a team. In this case, the model name follows directly after the org name. 
  3. Generate a Bearer token.
**Note:** The token is valid for 15 minutes. If the model is not in a team context, `/<<i>team</i>> is ommitted.`
Copy
Copied!
```
      
      
API_KEY=<API-key>
TOKEN=$(curl -s -u "\$oauthtoken":"$API_KEY" -H 'Accept:application/json' 'https://authn.nvidia.com/token?service=ngc&scope=group/ngc:<org>&group/ngc:<_org_>/<_team_>' | jq -r '.token')

    
```

  4. Download the model using curl. 
    1. Download the model ZIP using curl.
**Note:** If the model is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Model ZIP"
curl -LO 'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/models/<_model-name_>/versions/<_version_>/zip' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

Example model zip download:
Copy
Copied!
```
      
      
echo "Download Model ZIP"
curl -LO 'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/models/speechtotext_en_us_conformer_xl/versions/trainable_v4.0/zip' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

    2. Download a model file using curl 
**Note:** If the model is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Model file"
curl -LO --request GET 'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/models/<_model-name_>/versions/<_version_>/files/<_file-name_>' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

Example model file download:
Copy
Copied!
```
      
      
echo "Download Model file"
curl -LO --request GET 'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/models/speechtotext_en_us_conformer_xl/versions/trainable_v4.0/files/Conformer-CTC-XL_spe-128_en-US_Riva-ASR-SET-4.0.nemo' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

  5. Download the model using wget. 
    1. Download the model ZIP using wget.
**Note:** If the model is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Model ZIP"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/models/<_model-name_>/versions/<_version_>/zip' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

Example model zip download:
Copy
Copied!
```
      
      
echo "Download Model ZIP"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/models/speechtotext_en_us_conformer_xl/versions/trainable_v4.0/zip' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

    2. Download a model file using wget 
**Note:** If the model is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Model file"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/models/<_model-name_>/versions/<_version_>/files/<_file-name_>' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

Example model file download:
Copy
Copied!
```
      
      
echo "Download Model file"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/models/speechtotext_en_us_conformer_xl/versions/trainable_v4.0/files/Conformer-CTC-XL_spe-128_en-US_Riva-ASR-SET-4.0.nemo' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```



###  [16.5. Downloading Models via Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-webui)
How to download NGC models via the Web UI. 
###  [Downloading the Latest Version of a Model ](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-webui__context_cfl_pvd_nmb)
To download the latest version of a model to your local machine, performing the following. 
  1. Open the NGC UI, click **Catalog > Containers** from the left navigation and then locate and select the model you want to download. 
  2. Click the actions menu from the top right corner of the model detail page and then click **Download <version>**. 


**Example**
![ngc-model-download.png](https://docscontent.nvidia.com/dims4/default/a319f1b/2147483647/strip/true/crop/1128x346+0+0/resize/1128x346!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-model-download.png)
###  [Downloading a Specific Version of a Model](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-webui__section_ps3_rth_nmb)
To download a specific version of a model, performing the following. 
  1. Open the NGC UI, click **Models** from the top content type ribbon and then locate and click the model you want to download. 
  2. Click the Version History tab, then click the actions icon for the version to download and then click **Download**. 


The following diagram illustrates the steps. 
![ngc-model-version.png](https://docscontent.nvidia.com/dims4/default/c265243/2147483647/strip/true/crop/1109x600+0+0/resize/1109x600!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-model-version.png)
###  [16.6. NVIDIA Signed Models in the NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models)
This chapter provides NGC end users with guidance on locating signed models in the NGC Catalog and verifying the NVIDIA signature to confirm their authenticity and trusted origin. 
Software signing is a critical security feature that verifies the authenticity and integrity of distributed software. It ensures that the software originates from a trusted publisher and has not been altered after signing. This process helps users determine which software to trust and allows for secure execution. 
Model signing applies a digital signature to verify the model's origin and ensure its files remain unaltered. NVIDIA has integrated the [_OpenSSF_](https://openssf.org/)model signing framework into the NGC Catalog to offer enhanced security to our users. Beginning in April 2025, all NVIDIA models published on the NGC Catalog will be signed. 
###  [16.6.1. Checking for Signed Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking)
There are two methods to determine if a model is signed: through the NGC Catalog's user interface (UI) or via the NGC Command-Line Interface (CLI). 
###  [16.6.2. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking-ui)
Click on **Catalog > Models** from the left navigation menu. Select a model to view the details. On the details page, you will see the **Signed Model** badge on the left panel and the **Signed** badge on the pane in the **Version History** tab. 
![model-signing-dashboard.png](https://docscontent.nvidia.com/dims4/default/8879962/2147483647/strip/true/crop/1999x1115+0+0/resize/1440x803!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fmodel-signing-dashboard.png)
###  [16.6.3. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking-cli)
To find a signed model using the CLI, issue the following: 
Copy
Copied!
```
      
      
$ ngc registry model list <model_name>

    
```

**Example** : List all models with name containing 'tao': 
Copy
Copied!
```
      
      
$ ngc registry image list 'nvidia/tao/*'

    
```

If the model has a signed version, you can see a value `True` populated in the last **Has Signed Version** column. 
![model-signing-model-list.png](https://docscontent.nvidia.com/dims4/default/6ce262b/2147483647/strip/true/crop/1999x322+0+0/resize/1440x232!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fmodel-signing-model-list.png)
###  [16.6.4. Finding NVIDIA's Root Certificate](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-finding-root-certificate)
The NVIDIA Model Signing Root Certificate can be used to validate its authenticity. 
You can download the root certificate from the API using the following link: <https://api.ngc.nvidia.com/v2/catalog/models/public-key>. 
Copy
Copied!
```
      
      
-----BEGIN CERTIFICATE-----
MIICLjCCAbSgAwIBAgIUD8GTT5Xr1JC6tltkzsXnMzO1tAwwCgYIKoZIzj0EAwMw
RTELMAkGA1UEBhMCVVMxDzANBgNVBAoMBk5WSURJQTElMCMGA1UEAwwcTlZJRElB
IE1vZGVsIFNpZ25pbmcgUm9vdCBDQTAgFw0yNTAzMDcxNjU4MzFaGA8yMDU1MDIy
ODE2NTgzMVowRTELMAkGA1UEBhMCVVMxDzANBgNVBAoMBk5WSURJQTElMCMGA1UE
AwwcTlZJRElBIE1vZGVsIFNpZ25pbmcgUm9vdCBDQTB2MBAGByqGSM49AgEGBSuB
BAAiA2IABNAUiPGna2UfkGyEcdWjpPP9XH0Y5Q5OXdCag/QDzJTb/v/KHqHGT8bY
Kc13PWEtx6FXhEhoYGy/D53hRS1m56ulGrbwUSbjMzQ+FFQCDiYaN5GgglP2MZUX
/cYN5s/bUaNjMGEwHQYDVR0OBBYEFJYhbAEcpVyxvlOPkUMo03mjrVCPMB8GA1Ud
IwQYMBaAFJYhbAEcpVyxvlOPkUMo03mjrVCPMA8GA1UdEwEB/wQFMAMBAf8wDgYD
VR0PAQH/BAQDAgEGMAoGCCqGSM49BAMDA2gAMGUCMBrmk2HCI4B+LxssWntsfTqu
QRoh8Po8mkyhhChK16Ye5O6esHLerO7rwyJ7DOgCaQIxAOZmzHMhxsJtJIlSng+K
R+IB/Axwza1teUJdN5vWdsjbj8g7hja2rauePEjQB2AuNw==
-----END CERTIFICATE-----

    
```

###  [Verifying Model Signature](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed_models_verifying_model_signature)
NVIDIA has been actively collaborating with the Open Source Security Foundation ([OpenSSF](https://openssf.org/)) to enhance the security of artificial intelligence (AI) and machine learning (ML) models through initiatives like model signing. 
NVIDIA’s model signing provides a secure and transparent way to sign, verify, and protect software artifacts and AI models. 
####  Download Verification Tools 
The Git repository at [sigstore/model-transparency](https://github.com/sigstore/model-transparency.git) contains all the necessary tools required to verify a signed model. 
####  Downloading Model Version and Signature 
To download a specific version of a model, performing the following. 
**Example**
Copy
Copied!
```
      
      
$ ngc registry model download-version "nvidia/tao/dashcamnet:pruned_onnx_v1.0.5"

    
```

The sample output is: 
Copy
Copied!
```
      
      
{
 "download_end": "2025-03-17 09:50:50",
 "download_start": "2025-03-17 09:50:48",
 "download_time": "2s",
 "files_downloaded": 4,
 "local_path": "C:\\Users\\NVIDIA\\dashcamnet_vpruned_onnx_v1.0.5",
 "size_downloaded": "5.24 MB",
 "status": "COMPLETED"
}

    
```

To download a signature of a specific model, performing the following. 
**Example**
Copy
Copied!
```
      
      
$ ngc registry model download-version-signature "nvidia/tao/dashcamnet:pruned_onnx_v1.0.5"

    
```

The sample output is: 
Copy
Copied!
```
      
      
{
  "local_path": "C:\\Users\\NVIDIA/dashcamnet_vpruned_onnx_v1.0.5\\result.sigstore",
  "status": "COMPLETED"
}

    
```

####  Verifying Model Version Signature 
Navigate to the downloaded `model-transparency-main` directory and run the command: 
Copy
Copied!
```
      
      
$ C:\Users\NVIDIA\Downloads\model-transparency-main\model-transparency-main>
python verify.py --sig_path $sig_path --model_path $model_path pki --root_certs $public_key

    
```

where 
  * <`sig_path`>: Path to result.sigstore of downloaded model 
  * <`model_path`>: Path of downloaded model 
  * <`public_key`>: Path of public key downloaded from endpoint--<https://api.ngc.nvidia.com/v2/catalog/models/public-key>


The expected output is as follows: 
Copy
Copied!
```
      
      
python ./src/verify.py --sig_path \users\NVIDIA\dashcamnet_vpruned_onnx_v1.0.5\result.sigstore --model_path \Users\NVIDIA\dashcamnet_vpruned_onnx_v1.0.5 pki --root_certs \Users\NVIDIA\Downloads\publicKey.pem
INFO:__main__:Creating verifier for pki
INFO:__main__:Verifying model signature from \users\NVIDIA\dashcamnet_vpruned_onnx_v1.0.5\result.sigstore
INFO:__main__:all checks passed

    
```

## [17. Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-resources)
Description of NGC resources, their purpose, and how to use them. 
###  [17.1. What are Resources?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-what-are)
NGC resources offer documentation, code samples, and many other assets such as Jupyter Notebooks, deployment pipelines, and step-by-step instructions and scripts for creating deep learning models. These scripts have sample performance and accuracy metrics that allow you to compare your results. These scripts provide expert guidance on building DL models for image classification, language translation, text-to-speech, and more. Data scientists can quickly build performance-optimized models by easily adjusting the hyperparameters. 
###  [17.2. Searching and Filtering Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-resources)
To view NGC resources, navigate to **Catalog** > **Resources** in the left menu. Use the search bar at the top of the page to filter on resources or sort the list using the criteria from the dropdown menu. You can refine your search by utilizing the filters under Use Case, NVIDIA Platform, NVIDIA AI Enterprise, and many others. The descriptions for the filtering options are as follows: 
  * **Use Case** : Choose from the available common use cases. 
  * **NVIDIA Platform** : Choose from Clara, DeepStream, TensorFlow, and many others. 
  * **NVIDIA AI Enterprise Support** : Select this option to find publicly available resources supported by NVIDIA AI Enterprise. 
  * **NVIDIA AI Enterprise** : Choose products under this to see entitled entities. 
  * **Quick Deploy** : Select this option to find containers to quickly deploy your artifacts in a Jupyter environment. 
  * **Framework** : Filter by framework such as MXNet or NeMo. 
  * **Industry** : Select by available industries. 
  * **Solution** : Select the solution that closely matches your use case. 
  * **Publisher** : Filter by publisher. 
  * **Type** : Filter by type. 
  * **Language** : Select by language. 
  * **Other** : Miscellaneous options. 


The following example page shows the search and filtering options available when logging in as a guest user: 
![ngc-catalog-containers-resources-guest-ann.png](https://docscontent.nvidia.com/dims4/default/397b6c6/2147483647/strip/true/crop/1339x953+0+0/resize/1339x953!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-containers-resources-guest-ann.png)
###  [17.3. Downloading Resources via the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading)
To download a resource from the registry to your local disk, specify the resource name and version. 
Copy
Copied!
```
      
      
$ ngc registry resource download-version nvidia/<_resource-name:version_>

    
```

**Example** : Downloading a resource to the current directory. 
Copy
Copied!
```
      
      
$ ngc registry resource download-version nvidia/gnmt_v2_for_tensorflow:1

    
```

The following is an example showing the output confirming completion of the download: 
Copy
Copied!
```
      
      
Downloaded 130.6 KB in 1s, Download speed: 130.6 KB/s
----------------------------------------------------
Transfer id: gnmt_v2_for_tensorflow_v1 Download status: Completed.
Downloaded local path: C:\gnmt_v2_for_tensorflow_v1
Total files downloaded: 35
Total downloaded size: 130.6 KB
Started at: 2019-03-20 11:24:00.168000
Completed at: 2019-03-20 11:24:01.176000
Duration taken: 1s seconds
----------------------------------------------------

    
```

The model is downloaded to a folder that corresponds to the model name in the current directory. You can specify another path using the -d option. 
**Example** : Downloading a resource to a specific directory (/resources). 
Copy
Copied!
```
      
      
$ ngc registry resource download-version nvidia/gnmt_v2_for_tensorflow:1 -d ./resources

    
```

Copy
Copied!
```
      
      
Downloaded 130.6 KB in 1s, Download speed: 130.6 KB/s
----------------------------------------------------
Transfer id: gnmt_v2_for_tensorflow_v1 Download status: Completed.
Downloaded local path: C:\resources\gnmt_v2_for_tensorflow_v1
Total files downloaded: 35
Total downloaded size: 130.6 KB
Started at: 2019-03-20 11:24:00.168000
Completed at: 2019-03-20 11:24:01.176000
Duration taken: 1s seconds
----------------------------------------------------

    
```

###  [17.4. Downloading Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading-wget)
###  [17.4.1. Downloading Guest Access Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-guest-access-resources-via-wget)
How to download guest access resources via WGET/cURL. 
To get a copy of a single file from an NGC Resource via wget/curl you can use the URL provided in the NGC UI. 
  1. Open the NGC UI, click **Resources** from the left navigation menu and then locate and click the resource you want to download. 
![ngc-wget-resources.png](https://docscontent.nvidia.com/dims4/default/092d09a/2147483647/strip/true/crop/1638x948+0+0/resize/1440x833!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-resources.png)
  2. Click the **Download** button on the top right or navigate to the **File Browser** tab. 
![ngc-wget-download-resource.png](https://docscontent.nvidia.com/dims4/default/1d74daa/2147483647/strip/true/crop/1209x453+0+0/resize/1209x453!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-download-resource.png)
  3. Select the **Copy curl cmd** or **Copy wget cmd** to copy the relevant code to the clipboard.
![ngc-wget-resource-copy-curl-cmd.png](https://docscontent.nvidia.com/dims4/default/5f5e766/2147483647/strip/true/crop/1193x512+0+0/resize/1193x512!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-wget-resource-copy-curl-cmd.png)


The following will be added to your clipboard for the `wget` command: 
Copy
Copied!
```
      
      
wget --content-disposition 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/tao/tao-converter/v5.1.0_8.6.3.1_x86/files?redirect=true&path=tao-converter' -O tao-converter

    
```

Similarly, the following will be added to your clipboard for the `curl` command: 
Copy
Copied!
```
      
      
curl -LO 'https://api.ngc.nvidia.com/v2/resources/org/nvidia/team/tao/tao-converter/v5.1.0_8.6.3.1_x86/files?redirect=true&path=tao-converter'

    
```

###  [17.4.2. Downloading Authenticated Access Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-resources-via-wget-authenticated-access)
How to download authenticated access resources via WGET/cURL. 
  1. Obtain an NGC API Key. See [Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-api-key). This will be referred to as <_API-key_ > below.
  2. Find orgs and teams scope and resource name, resource version.
In the example below, the <_org_ > is **nvidia** and <_team_ > is **riva** , <_resource-name_ > is **riva_quickstart** , <_version_ > is **2.15.0** , <_file-name_ > is **nemo2riva-2.15.0-py3-none-any.whi**
![ngc-catalog-download-auth-access-resources.png](https://docscontent.nvidia.com/dims4/default/cd9470f/2147483647/strip/true/crop/1306x871+0+0/resize/1306x871!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-download-auth-access-resources.png)
  3. Generate a Bearer token.
**Note:** The token is valid for 15 minutes. If the resource is not in a team context, `/<<i>team</i>> is ommitted.`
Copy
Copied!
```
      
      
API_KEY=<API-key>
TOKEN=$(curl -s -u "\$oauthtoken":"$API_KEY" -H 'Accept:application/json' 'https://authn.nvidia.com/token?service=ngc&scope=group/ngc:<org>&group/ngc:<_org_>/<_team_>' | jq -r '.token')

    
```

  4. Download the resource using curl. 
    1. Download the resource ZIP using curl.
**Note:** If the resource is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Resource ZIP"
curl -LO 'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/resources/<_resource-name_>/versions/<_version_>/zip' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

Example resource zip download:
Copy
Copied!
```
      
      
echo "Download Resource ZIP"
curl -LO 'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/resources/riva_quickstart/versions/2.9.0/zip' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

    2. Download a resource file using curl.
**Note:** If the resource is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Resource file"
curl -LO --request GET 'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/reources/<_resource-name_>/versions/<_version_>/files/<_file-name_>' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

Example resource file download:
Copy
Copied!
```
      
      
echo "Download Resource file"
curl -LO --request GET 'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/resources/riva_quickstart/versions/2.9.0/files/riva_init.sh' -H "Authorization: Bearer ${TOKEN}" -H "Content-Type: application/json"

    
```

  5. Download the resource using wget. 
    1. Download the resource ZIP using wget.
**Note:** If the resource is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Resource ZIP"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/resources/<_resource-name_>/versions/<_version_>/zip' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

Example resource zip download:
Copy
Copied!
```
      
      
echo "Download Resource ZIP"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/resources/riva_quickstart/versions/2.9.0/zip' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

    2. Download a resource file using wget
**Note:** If the resource is not in a team context, `team/<<i>team</i>>/` is omitted. 
Copy
Copied!
```
      
      
echo "Download Resource file"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/<_org_>/team/<_team_>/resources/<_resource-name_>/versions/<_version_>/files/<_file-name_>' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```

Example resource file download:
Copy
Copied!
```
      
      
echo "Download Resource file"
wget --header="Authorization: Bearer $TOKEN" \
--header="Content-Type: application/json" \
'https://api.ngc.nvidia.com/v2/org/nvidia/team/riva/resources/riva_quickstart/versions/2.9.0/files/riva_quickstart.sh' \
2>&1 \
| awk '/Location:/ {print $2}' \
| xargs wget --content-disposition

    
```



###  [17.5. Downloading Resources via Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading-web)
  1. From a browser, go to the [NGC Catalog](https://catalog.ngc.nvidia.com) website. 
  2. Sign in. Refer to [Registering and Activating Your NGC Account](https://docs.nvidia.com/ngc/ngc-catalog-user-guide/index.html#registering-activating-ngc-account). 
  3. Click **Resources** from the left navigation menu. 
![resources-menu-left-nav.png](https://docscontent.nvidia.com/dims4/default/db3e1f7/2147483647/strip/true/crop/965x469+0+0/resize/965x469!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fresources-menu-left-nav.png)
You will see a page with available Resources. 
  4. Select one of the Resource cards. 
The details page provides additional information for each Resource.
![ngc-catalog-resource-details.png](https://docscontent.nvidia.com/dims4/default/49e10fe/2147483647/strip/true/crop/1099x696+0+0/resize/1099x696!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-resource-details.png)
The Download menu on the upper right corner offers three different ways to download the Resource. 
![ngc-catalog-resources-download.png](https://docscontent.nvidia.com/dims4/default/eb0655d/2147483647/strip/true/crop/210x184+0+0/resize/210x184!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-resources-download.png)
Click either **Browser (Direct Download)** to start the download, or **WGET** or **CLI** to copy the download commands to the clipboard. 
The **File Browser** tab lets you see the file content of the Resources. 
![ngc-catalog-resources-file-browser.png](https://docscontent.nvidia.com/dims4/default/e997a69/2147483647/strip/true/crop/1115x427+0+0/resize/1115x427!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-catalog-resources-file-browser.png)


## [18. Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-helm-charts)
Helm is an application package manager running on top of Kubernetes. This section describes how to use access Helm charts from the NGC Catalog. 
##  [Prerequisites](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-helm-charts__section_iv2_zrg_kkb)
These instructions assume the following prerequisites are met. 
  * Helm v 2.16.1 installed 
The helm push plugin does not support Helm v3 yet - make sure you are using v2.16.x. 
See <https://github.com/helm/helm/releases/tag/v2.16.1> for the Helm download and installation instructions. 
  * NGC organization account 
See [Setting Up and Activating Your NGC Account](https://docs.nvidia.com/dgx/ngc-registry-for-dgx-user-guide/index.html#setting-up-ngc-registry) for instructions. 


###  [18.1. Setting Up an NGC Helm Repository](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setting-up-ngc-helm-repository)
  1. Obtain an NGC API Key.
See [Generating Your NGC API Key](https://docs.nvidia.com/dgx/ngc-registry-for-dgx-user-guide/index.html#generating-api-key) for instructions. 
  2. Export the API Key for use in commands.
Copy
Copied!
```
      
      
$ export NGC_API_KEY=<_your-api-key_>

    
```

  3. Add the NGC org to your Helm repository.
Copy
Copied!
```
      
      
$ helm repo add <_repo-name_> https://helm.ngc.nvidia.com/<_org-name_> --username=\$oauthtoken --password=$NGC_API_KEY

    
```

Where `<<i>repo-name</i>>` is a name of your choosing by which you will reference the repository. 


###  [18.2. Searching for Available Helm Charts in the NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-available-helm-charts)
To view a list of available Chart packages in your org, issue the following. 
Copy
Copied!
```
      
      
$ helm search <_repo-name_>

    
```

**Example**
Copy
Copied!
```
      
      
$ helm search nvidian

    
```

###  [18.3. Fetching Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#fetching-helm-charts)
To download (or "fetch") a Helm chart package from the repo, issue the following. 
Copy
Copied!
```
      
      
$ helm fetch <_repo-name_>/<_chart-name_>

    
```

###  [18.4. Using the NGC Website to View the List of Helm Charts and Get Fetch Commands](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#viewing-list-of-helm-charts)
From the NGC website you can 
  * View the contents of the Helm chart repository.
  * Get the push command for a specific Helm chart in the repository.


  1. From a browser, log in to https://ngc.nvidia.com.
  2. If you are a member of more than one org, select the one that contains the Helm charts that you are interested in, then click **Sign In**.
  3. Click **Helm Charts** from the left-side navigation pane.
![ngc-helm-charts-nav.png](https://docscontent.nvidia.com/dims4/default/c4c099d/2147483647/strip/true/crop/185x329+0+0/resize/185x329!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fngc-helm-charts-nav.png)
The page presents cards for each available Helm chart. 
![helm-chart-cards-example.png](https://docscontent.nvidia.com/dims4/default/1154ad7/2147483647/strip/true/crop/1622x794+0+0/resize/1440x705!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fhelm-chart-cards-example.png)
  4. Select one of the Helm chart cards.
The page for each Helm chart provides information about the chart.
![helm-chart-page-example.png](https://docscontent.nvidia.com/dims4/default/909e3be/2147483647/strip/true/crop/1148x790+0+0/resize/1148x790!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fhelm-chart-page-example.png)
The Fetch Commandsection shows the command to use for downloading the Helm chart package. 
Click either the **Fetch** download button from the upper right corner or the copy icon next to the fetch command to copy the fetch command to the clipboard. 
The **File Browser** tab lets you see the file content of the Helm chart package. 
![helm-chart-file-browser.png](https://docscontent.nvidia.com/dims4/default/d171102/2147483647/strip/true/crop/1160x426+0+0/resize/1160x426!/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-aa7a-d72d-abf5-fefbffad0000%2Fngc%2Fgpu-cloud%2Fngc-catalog-user-guide%2Fgraphics%2Fhelm-chart-file-browser.png)


## [19. SDK and AI Toolkits](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#sdk-ai-toolkits)
NVIDIA AI toolkits provide libraries and tools to train, fine-tune, optimize and deploy pre-trained NGC models across a broad domain of industries and AI applications. 
These include 
  * An [AI-assisted annotation tool](https://ngc.nvidia.com/catalog/containers/nvidia:clara-train-sdk) to help users label their datasets for training. 
  * A [transfer learning toolkit](https://ngc.nvidia.com/catalog/containers/nvidia:tlt-streamanalytics) to fine-tune pre-trained models with user data, saving the cost of training from scratch. 
  * [Federated learning](https://ngc.nvidia.com/catalog/containers/nvidia:clara-train-sdk) that preserves privacy by allowing users to collaborate and train AI models without sharing private data between clients. 
  * The [NeMo toolkit](https://ngc.nvidia.com/catalog/containers/nvidia:nemo) to quickly build state-of-the-art models for speech recognition and natural language processing. 
  * The Service Maker toolkit that exposes trained models as a gRPC service that can be scaled and easily deployed on a Kubernetes service. 
  * Models built using the toolkits can be integrated inside client applications and deployed in production with the software development kits offered by NVIDIA. These SDKs leverage [TensorRT](https://ngc.nvidia.com/catalog/containers/nvidia:tensorrt) and the [Triton Inference Server](https://ngc.nvidia.com/catalog/containers/nvidia:tritonserver) as foundational building blocks. 

NVIDIA provides AI toolkits and application frameworks targeted towards industries or specific use cases. These are listed in the table below. 
**Industry or AI Application**| **AI Toolkits**  
---|---  
Healthcare and Life Sciences| [NVIDIA Clara](https://developer.nvidia.com/clara)  
Streaming video analytics|  [NVIDIA Metropolis](https://www.nvidia.com/en-us/autonomous-machines/intelligent-video-analytics-platform/) [NVIDIA DeepStream](https://developer.nvidia.com/deepstream-sdk)  
Robotics| [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac-sim)  
5G acceleration| [NVIDIA Aerial](https://developer.nvidia.com/aerial-sdk)  
Recommender Systems| [NVIDIA Merlin](https://developer.nvidia.com/nvidia-merlin)  
Conversational AI| [NVIDIA Riva](https://developer.nvidia.com/riva)  
## [20. Deep Learning Frameworks](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#dl-frameworks)
Deep learning frameworks offer building blocks for designing, training and validating deep neural networks, through a high level programming interface. Widely used deep learning frameworks such as MXNet, PyTorch, TensorFlow and others rely on GPU-accelerated libraries such as cuDNN, NCCL and DALI to deliver high-performance multi-GPU accelerated training. 
Developers, researchers and data scientists can get easy access to NVIDIA optimized deep learning framework containers with deep learning examples, that are performance tuned and tested for NVIDIA GPUs. This eliminates the need to manage packages and dependencies or build deep learning frameworks from source 
###  [GPU Operator](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#unique_424980274)
The Operator Framework within Kubernetes takes operational business logic and allows the creation of an automated framework for the deployment of applications within Kubernetes using standard Kubernetes APIs and kubectl. The NVIDIA GPU Operator automates the management of all NVIDIA software components needed to provision GPUs within Kubernetes. NVIDIA, Red Hat, and others in the community have collaborated on creating the GPU Operator. The GPU Operator is an important component of the [_NVIDIA EGX_](https://www.nvidia.com/en-us/data-center/products/egx-edge-computing/) software-defined platform that is designed to make large-scale hybrid-cloud and edge operations possible and efficient. 
## [Notices](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#notices-header)
###  [](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#notice)
###  Notice 
THE INFORMATION IN THIS GUIDE AND ALL OTHER INFORMATION CONTAINED IN NVIDIA DOCUMENTATION REFERENCED IN THIS GUIDE IS PROVIDED "AS IS." NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE INFORMATION FOR THE PRODUCT, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE. Notwithstanding any damages that customer might incur for any reason whatsoever, NVIDIA's aggregate and cumulative liability towards customer for the product described in this guide shall be limited in accordance with the NVIDIA terms and conditions of sale for the product.
THE NVIDIA PRODUCT DESCRIBED IN THIS GUIDE IS NOT FAULT TOLERANT AND IS NOT DESIGNED, MANUFACTURED OR INTENDED FOR USE IN CONNECTION WITH THE DESIGN, CONSTRUCTION, MAINTENANCE, AND/OR OPERATION OF ANY SYSTEM WHERE THE USE OR A FAILURE OF SUCH SYSTEM COULD RESULT IN A SITUATION THAT THREATENS THE SAFETY OF HUMAN LIFE OR SEVERE PHYSICAL HARM OR PROPERTY DAMAGE (INCLUDING, FOR EXAMPLE, USE IN CONNECTION WITH ANY NUCLEAR, AVIONICS, LIFE SUPPORT OR OTHER LIFE CRITICAL APPLICATION). NVIDIA EXPRESSLY DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTY OF FITNESS FOR SUCH HIGH RISK USES. NVIDIA SHALL NOT BE LIABLE TO CUSTOMER OR ANY THIRD PARTY, IN WHOLE OR IN PART, FOR ANY CLAIMS OR DAMAGES ARISING FROM SUCH HIGH RISK USES.
NVIDIA makes no representation or warranty that the product described in this guide will be suitable for any specified use without further testing or modification. Testing of all parameters of each product is not necessarily performed by NVIDIA. It is customer's sole responsibility to ensure the product is suitable and fit for the application planned by customer and to do the necessary testing for the application in order to avoid a default of the application or the product. Weaknesses in customer's product designs may affect the quality and reliability of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this guide. NVIDIA does not accept any liability related to any default, damage, costs or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any manner that is contrary to this guide, or (ii) customer product designs.
Other than the right for customer to use the information in this guide with the product, no other license, either expressed or implied, is hereby granted by NVIDIA under this guide. Reproduction of information in this guide is permissible only if reproduction is approved by NVIDIA in writing, is reproduced without alteration, and is accompanied by all associated conditions, limitations, and notices.
###  [](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#trademarks)
###  Trademarks 
NVIDIA and the NVIDIA logo are trademarks and/or registered trademarks of NVIDIA Corporation in the United States and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.
© 2020-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved. Last updated on Mar 18, 2025.
Topics
  * [User Guide](https://docs.nvidia.com/ngc/gpu-cloud/index.html)
  * [User Guide](https://docs.nvidia.com/ngc/gpu-cloud/index.html#user-guide)
    * [NGC User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html)
      * [1. What is NVIDIA NGC?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#what-is-nvidia-ngc)
      * [2. Why NGC Software](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#why-ngc-software)
      * [3. NGC Organizations and Teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-orgs-and-teams)
        * [3.1. NVIDIA Cloud Accounts and NGC](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-cloud-accounts)
        * [3.2. NGC Teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-teams)
        * [3.3. NGC Org Owner and Other Org Users](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-org-owner-users)
          * [3.3.1. Adding NGC Users to an Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-adding-users)
          * [3.3.2. Updating User Roles](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-updating-user-roles)
          * [3.3.3. Removing a User from an NGC Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-removing-users)
          * [3.3.4. Securing the Owner Account with Multi-Factor Authentication](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-org-owner-securing)
          * [3.3.5. Contacting your Org Owner](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-org-owner-contacting)
        * [3.4. Transferring Your Product Activation Invitation](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-transfer-invitation)
      * [4. Accessing NGC Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#accessing-ngc-org)
        * [4.1. Activating Your NGC Product from an NGC Email Invitation](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-ea-product-activation)
          * [4.1.1. NGC Product Activation by Invitation - New User](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-product-activation-new-user)
          * [4.1.2. NGC Product Activation by Invitation - Existing User](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-product-activation-existing-user)
        * [4.2. Activating NGC Product from an NVIDIA Commercial Entitlement Certificate](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#accessing-ngc-comm-entitlement)
        * [4.3. Signing Up for a Free Individual NGC Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-sign-up-free-ind)
        * [4.4. Setting up your NCA Account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#sign-in-account-owner)
          * [4.4.1. Setting Up NCA Recovery Email](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#set-up-nca-recovery-email)
        * [4.5. Accepting an NCA Invitation to Access NGC](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#nv-account-new-user-from-invite)
      * [5. Using an External SSO for NGC Org Authentication](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-org-auth-sso)
        * [5.1. Federating IdP with NVIDIA Cloud Services](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-federating-idp)
        * [5.2. Authenticating and Managing User Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-user-auth-managing)
        * [5.3. NGC IdP Membership Rules](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-idp-rules)
      * [6. Activating Your Subscription (Offer Dependent)](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#activating-subscription)
      * [7. Switching Orgs or Team After Logging into NGC](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-org-team-switch)
      * [8. NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-api-keys)
        * [8.1. Supported NGC Applications and API Key Types](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#ngc-apps-api-keys)
        * [8.2. Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#generating-api-key)
          * [8.2.1. Generating a Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#generating-personal-api-key)
            * [8.2.1.1. Assigning Services to Your Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#assigning-services-personal-api-key)
            * [8.2.1.2. Generating a Legacy NGC API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#generating-legacy-api-key)
          * [8.2.2. Generating a Service API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#generating-service-api-key)
      * [9. Notification Services](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#notification-services)
      * [10. Appendix](https://docs.nvidia.com/ngc/gpu-cloud/ngc-user-guide/index.html#appendix)
  * [Catalog and Private Registry](https://docs.nvidia.com/ngc/gpu-cloud/index.html#catalog-and-private-registry)
    * [NGC Catalog User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html)
      * [1. What is the NGC Catalog?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#what-is-ngc-catalog)
      * [2. Terms and Concepts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#terms-and-concepts)
      * [3. Why NGC Software](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#why-ngc-software)
      * [4. Accessing NGC Software](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#accessing-ngc-software)
      * [5. Registering and Activating a New NGC Org to Obtain Authenticated Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#registering-activating-ngc-account)
        * [5.1. Signing Up for an NVIDIA Cloud Account and Activating an Individual NGC Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#account-signup)
        * [5.2. NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-api-keys)
          * [5.2.1. Supported NGC Applications and API Key Types](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-apps-api-keys)
          * [5.2.2. Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-api-key)
            * [5.2.2.1. Generating a Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-personal-api-key)
              * [5.2.2.1.1. Assigning Services to Your Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#assigning-services-personal-api-key)
              * [5.2.2.1.2. Generating a Legacy NGC API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-legacy-api-key)
            * [5.2.2.2. Generating a Service API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#generating-service-api-key)
      * [6. Introduction to the NGC Catalog and NGC CLIs](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#intro-to-ngc-cli)
        * [6.1. Installing NGC Catalog CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#installing-ngc-catalog-cli)
        * [6.2. Installing NGC Registry CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#installing-ngc-registry-cli)
      * [7. Docker Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvcontainers)
        * [7.1. What Is a Docker Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#whatiscont)
        * [7.2. Why Use A Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#whycont)
        * [7.3. Searching and Filtering Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-containers)
      * [8. NGC Container Images in NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-catalog-containers)
        * [8.1. Why NGC Container Images?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#why-ngc-container-images)
          * [8.1.1. NGC Container Security Policy](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-container-security-policy)
          * [8.1.2. NVIDIA Security Risk Scale](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-security-risk-scale)
          * [8.1.3. GPU-performance tests for NGC Catalog Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-performance-test)
        * [8.2. NVIDIA Container Toolkit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-container-toolkit)
        * [8.3. NVIDIA CUDA Toolkit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#cuda-toolkit-file)
        * [8.4. Running Singularity Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity)
          * [8.4.1. Prerequisites](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites)
          * [8.4.2. Converting to Singularity Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#converting-to-singularity-image)
          * [8.4.3. Running the Singularity Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#running-the-singularity-container)
            * [8.4.3.1. Directory Access](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-directory-access)
            * [8.4.3.2. Command Line Execution with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-command-line)
            * [8.4.3.3. Interactive Shell with Singularity](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#singularity-interactive-shell)
      * [9. Prerequisites for Using NGC Catalog Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-image-prerequisites)
        * [9.1. Prerequisites for Using NGC Containers on DGX Systems](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-dgx)
        * [9.2. Prerequisites for Using NGC Containers on Cloud Platforms](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-csp)
        * [9.3. Prerequisites for Using NGC Containers on Other NVIDIA GPUs](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#prerequisites-gpu)
        * [9.4. HPC Visualization Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-container)
          * [9.4.1. Prerequisites For HPC Visualization Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-prereq)
          * [9.4.2. Installing NVIDIA Docker 2.0](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#hpc-vis-docker2)
          * [9.4.3. ParaView With NVIDIA Holodeck](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-holodeck)
          * [9.4.4. ParaView With NVIDIA IndeX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index)
            * [9.4.4.1. Single-Machine With GLX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-single)
            * [9.4.4.2. Server Container With EGL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-server)
            * [9.4.4.3. GLX Client Connecting To A Server](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-index-client)
          * [9.4.5. ParaView With NVIDIA OptiX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix)
            * [9.4.5.1. Single-Machine Container With GLX](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-single)
            * [9.4.5.2. Server Container With EGL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-server)
            * [9.4.5.3. Running The GLX Client And Attaching To The Server](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-glx)
            * [9.4.5.4. Optional: Using The ParaView .config File](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#paraview-optix-config)
      * [10. Pulling NGC Containers from NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pullcontainer)
        * [10.1. Key NGC Container Registry Terminology](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#keyconcepts)
        * [10.2. Accessing And Pulling an NGC Container Image via the Docker CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#accessing_registry)
          * [10.2.1. Logging in to the NGC container registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#logging-in-to-ngc-registry)
          * [10.2.2. Pulling a Container from NGC Container Registry Using Docker CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pull_ngc_docker)
        * [10.3. Accessing and Pulling an NGC Catalog Container Using NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#access-container-via-ngc-cli)
          * [10.3.1. Viewing Container Image Information](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#viewing-container-image)
          * [10.3.2. Pulling a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#pushing-container)
      * [11. NGC Container Image Versions](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvdocimver)
      * [12. NVIDIA Signed Container Images in NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nv-container-signatures)
        * [12.1. Checking for Signed Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images)
          * [12.1.1. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images-ui)
          * [12.1.2. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#checking-signed-container-images-cli)
        * [12.2. Finding NVIDIA's Public Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key)
          * [12.2.1. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key-ui)
          * [12.2.2. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#finding-public-key-cli)
        * [12.3. Verifying NVIDIA's Signature](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#verifying-nv-signature)
          * [12.3.1. Using Cosign](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#using-cosign)
          * [12.3.2. Using an Admission Controller in Kubernetes Clusters](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#verifying-nv-signature-admission-controller)
      * [13. Running an NGC Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#runcont)
        * [13.1. Enabling GPU Support for NGC Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#gpu-support)
        * [13.2. Running NGC Containers with Runtime Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#nvdocrun)
          * [13.2.1. Specifying A User](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#specifyuser)
          * [13.2.2. Setting The Remove Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setremflag)
          * [13.2.3. Setting The Interactive Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setintflag)
          * [13.2.4. Setting The Volumes Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setvolflag)
          * [13.2.5. Setting The Mapping Ports Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setmapportflag)
          * [13.2.6. Setting The Shared Memory Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setincshmem)
          * [13.2.7. Setting The Restricting Exposure Of GPUs Flag](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setresgpuflag)
          * [13.2.8. Container Lifetime](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setstatusoption)
      * [14. Multi-Architecture Support for NGC Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#multi-arch-support)
      * [15. Customizing Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontfrm)
        * [15.1. Benefits And Limitations To Customizing A Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#benlimcustcont)
        * [15.2. Example 1: Building A Container From Scratch](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#buildcontscratch)
        * [15.3. Example 2: Customizing A Container Using Dockerfile](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockerfile)
        * [15.4. Example 3: Customizing A Container Using docker commit](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#custcontdockercommit)
        * [15.5. Example 4: Developing A Container Using Docker](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#extendingcont)
          * [15.5.1. Example 4.1: Package The Source Into The Container](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#unique_1584239657)
      * [16. Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-models)
        * [16.1. What are Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#models-what-are)
        * [16.2. Searching and Filtering Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-models)
        * [16.3. Downloading Models via NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-ngc-cli)
        * [16.4. Downloading Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-wget)
          * [16.4.1. Downloading Guest Access Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-guest-access-models-via-wget)
          * [16.4.2. Downloading Authenticated Access Models via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-wget-authenticated-access)
        * [16.5. Downloading Models via Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-models-via-webui)
        * [16.6. NVIDIA Signed Models in the NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models)
          * [16.6.1. Checking for Signed Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking)
          * [16.6.2. Using the NGC Catalog UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking-ui)
          * [16.6.3. Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-checking-cli)
          * [16.6.4. Finding NVIDIA's Root Certificate](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed-models-finding-root-certificate)
          * [16.6.5. Verifying Model Signature](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#signed_models_verifying_model_signature)
      * [17. Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-resources)
        * [17.1. What are Resources?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-what-are)
        * [17.2. Searching and Filtering Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-resources)
        * [17.3. Downloading Resources via the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading)
        * [17.4. Downloading Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading-wget)
          * [17.4.1. Downloading Guest Access Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-guest-access-resources-via-wget)
          * [17.4.2. Downloading Authenticated Access Resources via WGET/cURL](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#download-resources-via-wget-authenticated-access)
        * [17.5. Downloading Resources via Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#resources-downloading-web)
      * [18. Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#ngc-helm-charts)
        * [18.1. Setting Up an NGC Helm Repository](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#setting-up-ngc-helm-repository)
        * [18.2. Searching for Available Helm Charts in the NGC Catalog](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#searching-available-helm-charts)
        * [18.3. Fetching Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#fetching-helm-charts)
        * [18.4. Using the NGC Website to View the List of Helm Charts and Get Fetch Commands](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#viewing-list-of-helm-charts)
      * [19. SDK and AI Toolkits](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#sdk-ai-toolkits)
      * [20. Deep Learning Frameworks](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#dl-frameworks)
        * [20.1. GPU Operator](https://docs.nvidia.com/ngc/gpu-cloud/ngc-catalog-user-guide/index.html#unique_424980274)
    * [NGC Private Registry User Guide](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html)
      * [1. NGC Private Registry for Enterprise](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-registry-overview)
      * [2. Getting Started](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#getting-started)
        * [2.1. Obtaining a Private Registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#obtaining-private-registry-dgx-customers)
        * [2.2. Activating a New NGC Account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#activating-ngc-user-account)
          * [2.2.1. Joining an NGC Org or Team with an Existing NVIDIA Account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-existing-account-setup)
          * [2.2.2. Joining an Org or Team with a New NVIDIA Account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-account-setup)
          * [2.2.3. Joining an Org as Org Owner](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-org-account-setup)
          * [2.2.4. Joining an Org or Team with an External SSO Company Account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-sso-account-setup)
          * [2.2.5. Switching Orgs or Team After Logging into NGC](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-org-team-switch)
        * [2.3. NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-api-keys)
          * [2.3.1. Supported NGC Applications and API Key Types](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-apps-api-keys)
          * [2.3.2. Generating NGC API Keys](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#generating-api-key)
            * [2.3.2.1. Generating a Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#generating-personal-api-key)
              * [2.3.2.1.1. Assigning Services to Your Personal API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#assigning-services-personal-api-key)
              * [2.3.2.1.2. Generating a Legacy NGC API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#generating-legacy-api-key)
            * [2.3.2.2. Generating a Service API Key](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#generating-service-api-key)
        * [2.4. Managing Users and Teams in NGC](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#administrator-instructions)
          * [2.4.1. NGC Registry User Roles](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#user-roles)
          * [2.4.2. Creating Teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#creating-teams)
          * [2.4.3. Creating Users](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#creating-users)
          * [2.4.4. Adding a New User to a Team](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#adding-users-to-teams)
          * [2.4.5. Adding an Existing User to a Team](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#adding-existing-user-to-team)
          * [2.4.6. Changing User Roles](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#changing-user-roles)
        * [2.5. Introduction to the NGC Catalog and NGC CLIs](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#intro-to-ngc-cli)
          * [2.5.1. Installing NGC Registry CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#installing-ngc-registry-cli)
          * [2.5.2. Managing Users and Teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-managing-users-teams)
            * [2.5.2.1. Inviting users to the organization’s NGC account](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-inviting-users)
            * [2.5.2.2. Creating teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-creating-teams)
            * [2.5.2.3. Adding users to teams](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-add-users-to-teams)
            * [2.5.2.4. Creating a team and adding a user in the same command](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-creating-team-user)
            * [2.5.2.5. Creating a team and adding a user in the same command](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#cli-user-roles-permissions)
      * [3. Docker Containers](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#nvcontainers)
        * [3.1. What Is A Docker Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#whatiscont)
        * [3.2. Why Use A Container?](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#whycont)
        * [3.3. Using NGC Container Registry from the Docker Command Line](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#using-ngc-registry-from-docker-command-line)
          * [3.3.1. Accessing the NGC Container Registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#accessing-ngc-registry)
          * [3.3.2. Uploading an NVIDIA Container Image onto Your System](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#loading-nvidia-docker-containers)
          * [3.3.3. Tagging and Pushing a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#tag-and-push-container-image)
        * [3.4. Using the Container Registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#using-container-registry)
          * [3.4.1. Viewing Container Image Information](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#viewing-container-image-info)
          * [3.4.2. Pulling a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#pushing-container)
          * [3.4.3. Pushing a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#unique_1173235415)
          * [3.4.4. Removing a Container Image](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#removing-container-image)
        * [3.5. Updating Container Metadata](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#updating-container-metadata)
          * [3.5.1. Updating Container Metadata via the NGC Website](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#updating-container-metadata-via-ui)
          * [3.5.2. Updating Container Metadata Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#updating-container-metadata-via-cli)
        * [3.6. Multi-architecture Support for NGC Container Images](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-container-multi-architecture-support)
      * [4. NGC Models](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-models)
        * [4.1. Creating New NGC Models Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#creating-new-model-via-cli)
        * [4.2. Creating a New Model Using the NGC Website](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#creating-new-model-via-ui)
        * [4.3. Uploading a New NGC Model Version Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#uploading-new-model-version-via-cli)
        * [4.4. Uploading an NGC Model Version Using the NGC Website](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#uploading-new-model-version-via-ui)
        * [4.5. Editing NGC Model Information Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#editing-model-info-via-cli)
        * [4.6. Editing NGC Model Information Using the NGC Website](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#editing-model-info-via-ui)
      * [5. NGC Resources](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-resources)
        * [5.1. Before You Begin](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#resources-before-you-begin)
        * [5.2. Uploading a Resource](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#resources-uploading)
        * [5.3. Updating a Resource](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#resources-updating)
        * [5.4. Resource Commands](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#resource-commands)
        * [5.5. Deleting a Resource](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#resources-deleting)
      * [6. NGC Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#ngc-helm-charts)
        * [6.1. Introduction to NGC and Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#introduction)
        * [6.2. Creating and Packaging a Helm Chart](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#creating-packaging-helm-chart)
        * [6.3. Manage Helm Charts Using the NGC Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#managing-helm-charts-using-ngc-ui)
          * [6.3.1. Viewing the List of Helm Charts and Getting Fetch Commands](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#viewing-list-of-helm-charts)
          * [6.3.2. Adding Helm Charts Using the NGC Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#adding-helm-charts-from-web-ui)
          * [6.3.3. Updating the Helm Chart Page From the Website](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#unique_1164434965)
          * [6.3.4. Removing Helm Charts from the Web UI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#removing-helm-charts-from-web-ui)
        * [6.4. Manage Helm Charts Using the NGC CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#managing-helm-charts-using-ngc-cli)
          * [6.4.1. Searching for Available Helm Charts in an Org](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#searching-available-helm-charts-in-org)
          * [6.4.2. Fetching Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#fetching-helm-charts-ngc-cli)
          * [6.4.3. Adding Helm Charts to a Private Registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#adding-helm-charts-to-private-registry-ngc-cli)
          * [6.4.4. Getting Information about a Helm Chart](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#getting-helm-chart-info-ngc-cli)
          * [6.4.5. Pushing a Helm Chart](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#pushing-helm-chart-ngc-cli)
          * [6.4.6. Listing Helm Chart Versions](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#listing-helm-chart-versions-ngc-cli)
          * [6.4.7. Removing Helm Charts from a Private Registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#removing-helm-charts-from-private-registry-ngc-cli)
        * [6.5. Manage Helm Charts Using the NGC API](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#managing-helm-charts-using-ngc-api)
          * [6.5.1. Updating Information on the Helm Chart Page](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#updating-helm-page-information)
          * [6.5.2. Deleting Helm Charts Using the NGC API](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#removing-helm-charts-from-repo)
        * [6.6. Manage Helm Charts Using the Helm CLI](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#managing-helm-charts-using-helm-cli)
          * [6.6.1. Setting Up an NGC Helm Repository](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#setting-up-ngc-helm-repository)
          * [6.6.2. Searching for Available Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#searching-available-helm-charts)
          * [6.6.3. Fetching Helm Charts](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#fetching-helm-charts)
          * [6.6.4. Adding Helm Charts to a Private NGC Org/Team](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#adding-helm-charts-to-repo)
          * [6.6.5. Removing Helm Charts from a Private NGC Org/Team](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#removing-helm-charts-from-private-org-team)
      * [7. Private Registry Quotas and Limits](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#private-registry-size-limits)
      * [8. Getting Support for NGC container registry](https://docs.nvidia.com/ngc/gpu-cloud/ngc-private-registry-user-guide/index.html#get-support-for-ngc-registry)


  * Corporate Info
    * [NVIDIA.com Home](https://www.nvidia.com/en-us/)
    * [About NVIDIA](https://www.nvidia.com/en-us/about-nvidia/)
  * ‎NVIDIA Developer
    * [Developer Home](https://developer.nvidia.com/)
    * [Blog](https://blogs.nvidia.com/)
  * Resources
    * [Contact Us](https://www.nvidia.com/en-us/contact/)
    * [Developer Program](https://developer.nvidia.com/developer-program)


[Privacy Policy ](https://www.nvidia.com/en-us/about-nvidia/privacy-policy/)| [Manage My Privacy](https://www.nvidia.com/en-us/about-nvidia/privacy-center/) | [Do Not Sell or Share My Data](https://www.nvidia.com/en-us/preferences/start/) | [Terms of Service](https://www.nvidia.com/en-us/about-nvidia/terms-of-service/) | [Accessibility](https://www.nvidia.com/en-us/about-nvidia/accessibility/) | [Corporate Policies](https://www.nvidia.com/en-us/about-nvidia/company-policies/) | [Product Security](https://www.nvidia.com/en-us/product-security/) | [Contact](https://www.nvidia.com/en-us/contact/)
Copyright © 2025 NVIDIA Corporation
Close
content here 
