set yyyy=%date:~,4%
set mm=%date:~5,2%
set day=%date:~8,2% 
set "YYYYmmdd=%yyyy%%mm%%day%" 
REM 替换空格
set "YYYYmmdd=%YYYYmmdd: =0%"

set hh=%time:~0,2%
set mi=%time:~3,2%
set ss=%time:~6,2% 
set "hhmiss=%hh%%mi%%ss%"

REM 替换空格
set "hhmiss=%hhmiss: =0%"

set VER="VER_COMMIT_TIME_%YYYYmmdd%_%hhmiss%"

REM git command
git add *
git commit  -m "%VER%"
git push -u DataMgr "liu.changsheng@sfit.shfe.com.cn"