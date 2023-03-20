This project is an attempt to relay message beased on self-defined chunks in Portable Network Graphic files.

It was said in PNG Specification that self-defined chunks should not contain human readible message. If you truely want to do so, put it in tExt Chunk. However, considering that will ruin the original tExt message, I decided to use self-defined chunks.

Another reason for self-defined chunk's robustness. Indeed, messages can be simply appended to the end of png files and work the same, as if they are in chunks. Yet, if the image is edited even just a pixel, the message is losted. Appended messages are not part of the image, so when image editor rewrites the file, they would be overwritten.

First commit:
I managed to insert self-defined chunks in image, image viewers can decode it just like other images. There is one problem: I hand written it. I must automize the process unless I want to write chunk layout myself every time.

Second commit: 
I wrote an algorithm to automatical format input content into a self-defined chunk. The core algorithm is done.