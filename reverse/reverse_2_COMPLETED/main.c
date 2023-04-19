undefined8 main(int param_1,long param_2)

{
  void **ppvVar1;
  size_t len;
  void *pvVar2;
  undefined8 info_struct;
  undefined8 read_struct;
  byte local_39;
  int img_h;
  undefined4 img_w;
  FILE *img;
  long *h_left_shift_with_3;
  int j;
  int i;
  
  h_left_shift_with_3 = (long *)0x0;
  if (param_1 < 2) {
    puts("Missing argument");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  len = strlen(*(char **)(param_2 + 8));
  if (len != 0x26) {
    puts("Invalid length");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  img = fopen("image.png","rb");
  read_struct = png_create_read_struct("1.6.38",0,0,0);
  info_struct = png_create_info_struct(read_struct);
  png_init_io(read_struct,img);
  png_read_info(read_struct,info_struct);
  img_w = png_get_image_width(read_struct,info_struct);
  img_h = png_get_image_height(read_struct,info_struct);
  png_read_update_info(read_struct,info_struct);
  h_left_shift_with_3 = (long *)malloc((long)img_h << 3);
  for (i = 0; i < img_h; i = i + 1) {
    len = png_get_rowbytes(read_struct,info_struct);
    ppvVar1 = (void **)(h_left_shift_with_3 + i);
    pvVar2 = malloc(len);
    *ppvVar1 = pvVar2;
  }
  png_read_image(read_struct,h_left_shift_with_3);
  j = 0;
  while( true ) {
    if (0x25 < j) {
      fclose(img);
      png_destroy_read_struct(&read_struct,&info_struct,0);
      puts("Your flag is correct!");
      return 0;
    }
    local_39 = *(byte *)((long)(j << 2) + h_left_shift_with_3[1]) ^
               *(byte *)((long)(j << 2) + *h_left_shift_with_3);
    if (local_39 != *(byte *)((long)j + *(long *)(param_2 + 8))) break;
    j = j + 1;
  }
  puts("Wrong flag...");
                    /* WARNING: Subroutine does not return */
  exit(1);
}