
# SSH Key Setup Guide for AWS EC2  

This guide walks you through the process of generating, formatting, and using RSA keys for secure SSH access to AWS EC2 instances.  

---

## **1. Generate RSA Key Pair**  
Run the following command to create a pair of RSA keys:  

```bash
ssh-keygen -t rsa
```  

- This generates a private key (`id_rsa`) and a public key (`id_rsa.pub`).  
- You will be prompted to specify a location to save the keys (default is `~/.ssh`).  
- Optionally, you can set a passphrase for additional security.  

---

## **2. Move to the .ssh Folder**  
Navigate to the folder containing your SSH keys:  

```bash
cd ~/.ssh
```  

---

## **3. Change the Passphrase and Format of the Private Key**  
To update the passphrase and convert the key to PEM format (required for compatibility with some tools):  

```bash
ssh-keygen -p -m PEM -f id_rsa
```  

- `-p`: Updates the passphrase of the private key.  
- `-m PEM`: Converts the key to PEM format.  
- `-f id_rsa`: Specifies the private key file to update.  

---

## **4. Set Up `authorized_keys`**  
To authorize the public key for SSH access:  

```bash
cp id_rsa.pub authorized_keys
```  

- The `authorized_keys` file contains a list of public keys allowed to access the system.  

---

## **5. Edit the Private Key for EC2**  
If you need to convert your private key for AWS EC2 compatibility:  

1. Open the private key using a text editor or the `cat` command:  
   ```bash
   cat id_rsa
   ```  

2. Copy the entire content of the `id_rsa` file.  

3. Open your `.pem` file in a text editor (e.g., VS Code):  
   - Paste the copied content.  
   - Ensure the file uses *LF* (Line Feed) format:  
     - In VS Code, check the bottom-right corner.  
     - If it says `CRLF`, click on it and change to `LF`.  

---

## **6. Use the Key with EC2**  
Ensure your `.pem` file has the correct permissions:  

```bash
chmod 400 ec2-pemfile.pem
```  

Connect to your EC2 instance:  

```bash
ssh -i ec2-pemfile.pem ec2-user@<EC2_INSTANCE_IP>
```  

---

## **Notes**  

1. **File Permissions:**  
   - Protect your private key (`id_rsa`) with restricted permissions:  
     ```bash
     chmod 600 ~/.ssh/id_rsa
     ```  

2. **Backup:**  
   - Keep your private key secure and back it up in a safe location.  
   - Never share your private key with anyone.  

---

By following this guide, you'll have a secure and properly formatted setup for using RSA keys with AWS EC2 instances.  

Need more help? Check out this [video walkthrough](https://www.youtube.com/watch?v=TwNqizhv7Cw).  

---  

**Happy Securing!**
