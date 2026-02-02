"""openers.py."""
import win32com.client

from agentic_vis.config import DEFAULT_XLSX_FILE_PATH


def full_control_open_pptx(filename: str, stoppable: bool = True) -> None:
    

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True

    presentation = app.Presentations.Open(filename)

    if stoppable:
        # Do stuff here...
        input("Press Enter to close the presentation and quit PowerPoint...")

    print ('closing presentation and quitting PowerPoint')
    presentation.Close()
    app.Quit()

import os
from typing import Tuple

def close_excel_if_open(
    filename: str,
    save_changes: bool = False,
    close_app: str = "never",  # "never" | "if_no_workbooks" | "always"
    save_all_before_quit: bool = False
) -> Tuple[bool, str]:
    """
    Attempts to close the given Excel workbook if it is open in Microsoft Excel (Windows).
    Optionally closes the Excel application instance as well.

    Parameters
    ----------
    filename : str
        Path to the file to check/close.
    save_changes : bool, optional
        Whether to save changes to the target workbook when closing it. Defaults to False.
    close_app : {"never", "if_no_workbooks", "always"}, optional
        - "never": do not quit Excel app (default).
        - "if_no_workbooks": quit Excel if no workbooks left open after closing the target.
        - "always": quit the attached Excel instance after closing the target (may affect other open workbooks).
    save_all_before_quit : bool, optional
        If close_app is "always" or "if_no_workbooks", determine whether to save all open workbooks
        before quitting Excel. Defaults to False.

    Returns
    -------
    (success, message) : Tuple[bool, str]
        success: True if the operation completed as intended (closed or confirmed not open).
        message: Description of what happened.

    Behavior
    --------
    1) Verifies Excel-like extensions.
    2) On Windows, attaches to a running Excel instance via COM without creating a new one.
    3) Closes the specific workbook if found in that instance.
    4) Depending on `close_app`, quits the Excel instance or not.
    5) If not found, falls back to a lock check to infer whether the file is in use elsewhere.
    """

    excel_exts = {".xls", ".xlsx", ".xlsm", ".xltx", ".xltm"}
    full_path = os.path.abspath(filename)
    _, ext = os.path.splitext(full_path)

    if ext.lower() not in excel_exts:
        return False, f"Not an Excel file (extension {ext}). No action taken."

    if not os.path.exists(full_path):
        return False, f"File does not exist: {full_path}"

    close_app = (close_app or "never").lower()
    if close_app not in {"never", "if_no_workbooks", "always"}:
        return False, f'Invalid close_app="{close_app}". Use "never", "if_no_workbooks", or "always".'

    is_windows = os.name == "nt"
    if is_windows:
        try:
            import win32com.client  # pywin32
            import pythoncom

            # Attach to a currently running Excel instance (do NOT start a new one)
            try:
                excel = win32com.client.GetActiveObject("Excel.Application")
            except Exception:
                excel = None

            if excel is not None:
                pythoncom.CoInitialize()

                target = os.path.normcase(os.path.normpath(full_path))
                found = False
                closed_target = False

                # Close the target workbook if found in this instance
                # Convert to list to avoid collection mutation during iteration
                for wb in list(excel.Workbooks):
                    try:
                        wb_path = os.path.normcase(os.path.normpath(wb.FullName))
                    except Exception:
                        continue
                    if wb_path == target:
                        found = True
                        wb.Close(SaveChanges=-1 if save_changes else 0)
                        closed_target = True
                        break  # Target closed; stop searching

                # Decide whether to quit the Excel instance
                quit_msg = ""
                if close_app == "always":
                    if save_all_before_quit:
                        _save_all_workbooks(excel)
                    excel.Quit()
                    quit_msg = " Excel application was closed (this instance)."

                elif close_app == "if_no_workbooks":
                    # If there are no workbooks left, quit the app
                    if excel.Workbooks.Count == 0:
                        if save_all_before_quit:
                            # No-op effectively, but keep the semantics
                            pass
                        excel.Quit()
                        quit_msg = " Excel application was closed (no workbooks remaining)."

                if closed_target:
                    return True, f"Closed workbook: {full_path} ({'saved' if save_changes else 'discarded changes'}).{quit_msg}"

                # Not found in this instance — might be in another Excel instance
                # Fall through to locking check for extra info.
        except ImportError:
            # pywin32 not installed; can't automate Excel
            pass
        except Exception as e:
            return False, f"Excel COM automation error: {e}"

    # Fallback: check if the file appears locked (likely open in another instance/process)
    locked, lock_msg = _is_file_locked(full_path)
    if locked:
        if is_windows:
            suffix = "Possibly open in another Excel instance or by another user/process."
        else:
            suffix = "COM automation not available on this platform."
        return False, f"The file appears to be locked. {suffix} {lock_msg}"

    return True, "The workbook does not appear to be open. No action needed."


def _save_all_workbooks(excel_app) -> None:
    """
    Saves all open workbooks in a given Excel Application instance.
    """
    try:
        for wb in list(excel_app.Workbooks):
            try:
                wb.Save()
            except Exception:
                # Ignore save issues per workbook to avoid blocking app quit
                pass
    except Exception:
        pass


def _is_file_locked(path: str) -> Tuple[bool, str]:
    """
    Heuristic: tries to open the file with read/write handle.
    If it fails due to a sharing violation or permission error, consider it locked.
    """
    try:
        fd = os.open(path, os.O_RDWR)
        try:
            with os.fdopen(fd, "rb+", closefd=False) as f:
                f.read(1)
        finally:
            os.close(fd)
        return False, "Successfully opened with read/write handle; not locked."
    except PermissionError as e:
        return True, f"PermissionError indicates a lock or insufficient rights: {e}"
    except OSError as e:
        msg = str(e)
        if "used by another process" in msg.lower() or "resource busy" in msg.lower():
            return True, f"OSError suggests the file is in use: {e}"
        return False, f"OSError but not a clear lock; assuming not locked: {e}"


if __name__ == '__main__':
    excel_file = DEFAULT_XLSX_FILE_PATH
    success, message = close_excel_if_open(excel_file, save_changes=False)
    print(success, message)

