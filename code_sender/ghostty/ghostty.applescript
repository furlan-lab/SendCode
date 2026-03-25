on run argv
    tell application "Ghostty"
        set term to focused terminal of selected tab of front window
        set cmd to (item 1 of argv) as string
        set commit to ((item 2 of argv) as string is "True")
        set start_pos to 1
        set len to length of cmd
        if len is greater than 1000 then
            set end_pos to 1000
        else
            set end_pos to len
        end if
        if len is greater than 0 then
            repeat
                input text (text start_pos thru end_pos of cmd) to term
                delay 0.1
                if end_pos is len then
                    exit repeat
                else
                    set start_pos to end_pos + 1
                    if len is greater than end_pos + 1000 then
                        set end_pos to end_pos + 1000
                    else
                        set end_pos to len
                    end if
                end if
            end repeat
        end if
        if commit then
            input text return to term
        end if
    end tell
end run
