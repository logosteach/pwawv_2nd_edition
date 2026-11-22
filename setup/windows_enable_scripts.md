# Enable PowerShell Scripts on Windows 11

If you use macOS or Linux, you can skip this page. It is only for Windows.

When you activate a Python virtual environment in PowerShell, Windows may block the activation script. This page shows you how to allow scripts for your own account, or just for one terminal window on a school or shared computer. The textbook links here so these steps are not repeated in every lesson.

## The Error You Might See

In the VS Code terminal on Windows, the shell is PowerShell. After you create a virtual environment, you activate it with:

```powershell
.venv\Scripts\activate
```

If scripts are blocked, PowerShell shows an error like this. The file path on your computer will look a little different:

```terminal
PS C:\Users\YourName\project_2> .venv\Scripts\activate
.venv\Scripts\activate : File C:\Users\YourName\project_2\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

The important words are **running scripts is disabled on this system**. PowerShell is pointing you to a setting called the *execution policy*.

## What Is an Execution Policy?

An execution policy is a safety setting in PowerShell. It decides whether scripts (files that end in `.ps1`) are allowed to run.

Windows turns this protection on by default so that a script you did not mean to run, especially one downloaded from the internet, cannot start by accident. On Windows 11, the default policy is `Restricted`, which lets you type commands one at a time but does not allow scripts. Activating a virtual environment runs a script named `Activate.ps1`, so the default setting blocks it.

## Check Your Current Settings

In PowerShell, type:

```powershell
Get-ExecutionPolicy -List
```

You will see a table of scopes. On a typical Windows 11 computer that has never been changed, it looks like this:

```terminal
        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser       Undefined
 LocalMachine       Undefined
```

`Undefined` means no special policy is set in that scope. When every scope is `Undefined`, Windows 11 uses `Restricted`, and scripts cannot run.

## The Fix for Your Own Account

This is the setting most students should use. It applies only to your user account, and you do not need administrator rights.

Type:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

PowerShell will ask you to confirm. The message looks like this:

```terminal
Execution Policy Change
The execution policy helps protect you from scripts that you do not trust. Changing the execution policy might expose you to the security risks described in the about_Execution_Policies help topic at https:/go.microsoft.com/fwlink/?LinkID=135170. Do you want to change the execution policy?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"):
```

Type `Y` and press Enter.

`RemoteSigned` means scripts you create on this computer, such as the virtual environment's `Activate.ps1`, can run. Scripts downloaded from the internet must be signed by a trusted publisher before they will run.

This change is saved for your account, so you should not have to set it again the next time you open a terminal.

## If You Are on a School or Shared Computer

If this is not your computer, or your school does not want settings changed, do not use the command above. Instead, you can allow scripts only in the current PowerShell window:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

Answer `Y` if you are asked to confirm.

This lasts only until you close that window. Stay in the same terminal and activate the virtual environment next. If you close the terminal, you will need to run the `Bypass` command again in the new window.

## Activate Your Virtual Environment Again

If you used the `CurrentUser` fix, close the terminal and open a new one in VS Code (on Windows, a new terminal is a new PowerShell window). Then go to your project folder and type:

```powershell
.venv\Scripts\activate
```

When it works, your prompt starts with `(.venv)`, like this:

```terminal
PS C:\Users\YourName\project_2> .venv\Scripts\activate
(.venv) PS C:\Users\YourName\project_2>
```

If you used the school-computer `Bypass` command, skip closing the terminal. Activate in that same window.

## How to Undo the Change

To remove the `CurrentUser` setting and go back to the Windows default, type:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope CurrentUser
```

Answer `Y` if you are asked to confirm. After that, scripts will be blocked again on a typical Windows 11 computer, and you will see the same error if you try to activate a virtual environment.

You do not need to undo the `Bypass` setting. It disappears when you close that PowerShell window.

## If It Still Doesn't Work

On some school or work computers, a *Group Policy* set by the administrator can override the commands on this page. If PowerShell says your setting was updated but is overridden by Group Policy, or if `Get-ExecutionPolicy -List` shows a value other than `Undefined` under `MachinePolicy` or `UserPolicy`, the computer is being managed for you.

Ask your instructor or the computer's owner for help. Do not try to get around school IT rules.

For more detail from Microsoft, see [about_Execution_Policies](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies).
