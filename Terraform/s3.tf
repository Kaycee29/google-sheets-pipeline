# create s3 bucket for weather API
resource "aws_s3_bucket" "google-sheet-data" {
  bucket = "kaycee-gs-data"

  tags = {
    Name        = "google-sheet-bucket"
    Environment = "Dev"
  }
}