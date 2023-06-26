# Set the source S3 bucket and directory path
$sourceBucket = "emotionet"
$sourceDirectory = "Images"

# Set the destination directory path
$destinationDirectory = "D:\Programs\Projects\femo\project\EmotioNet\whole"

# Loop through the folder names and download each folder
for ($i = 2382; $i -le 2790; $i++) {
    $folderName = "N_000000$($i.ToString().PadLeft(4, '0'))"
    $destinationPath = Join-Path -Path $destinationDirectory -ChildPath $folderName
    aws s3 sync s3://$sourceBucket/$sourceDirectory/$folderName $destinationPath
}
