from django.db import models

# Create your models here.

class cltt(models.Model):
	clno = models.PositiveSmallIntegerField()

	clse = models.CharField(max_length = 10)

	cltime = models.CharField(max_length = 150)

	m0 = models.CharField(max_length = 150, null=True, blank=True)
	m1 = models.CharField(max_length = 150, null=True, blank=True)
	m2 = models.CharField(max_length = 150, null=True, blank=True)
	m3 = models.CharField(max_length = 150, null=True, blank=True)
	m4 = models.CharField(max_length = 150, null=True, blank=True)
	m5 = models.CharField(max_length = 150, null=True, blank=True)
	m6 = models.CharField(max_length = 150, null=True, blank=True)
	m7 = models.CharField(max_length = 150, null=True, blank=True)
	m8 = models.CharField(max_length = 150, null=True, blank=True)

	t0 = models.CharField(max_length = 150, null=True, blank=True)
	t1 = models.CharField(max_length = 150, null=True, blank=True)
	t2 = models.CharField(max_length = 150, null=True, blank=True)
	t3 = models.CharField(max_length = 150, null=True, blank=True)
	t4 = models.CharField(max_length = 150, null=True, blank=True)
	t5 = models.CharField(max_length = 150, null=True, blank=True)
	t6 = models.CharField(max_length = 150, null=True, blank=True)
	t7 = models.CharField(max_length = 150, null=True, blank=True)
	t8 = models.CharField(max_length = 150, null=True, blank=True)

	w0 = models.CharField(max_length = 150, null=True, blank=True)
	w1 = models.CharField(max_length = 150, null=True, blank=True)
	w2 = models.CharField(max_length = 150, null=True, blank=True)
	w3 = models.CharField(max_length = 150, null=True, blank=True)
	w4 = models.CharField(max_length = 150, null=True, blank=True)
	w5 = models.CharField(max_length = 150, null=True, blank=True)
	w6 = models.CharField(max_length = 150, null=True, blank=True)
	w7 = models.CharField(max_length = 150, null=True, blank=True)
	w8 = models.CharField(max_length = 150, null=True, blank=True)

	h0 = models.CharField(max_length = 150, null=True, blank=True)
	h1 = models.CharField(max_length = 150, null=True, blank=True)
	h2 = models.CharField(max_length = 150, null=True, blank=True)
	h3 = models.CharField(max_length = 150, null=True, blank=True)
	h4 = models.CharField(max_length = 150, null=True, blank=True)
	h5 = models.CharField(max_length = 150, null=True, blank=True)
	h6 = models.CharField(max_length = 150, null=True, blank=True)
	h7 = models.CharField(max_length = 150, null=True, blank=True)
	h8 = models.CharField(max_length = 150, null=True, blank=True)

	f0 = models.CharField(max_length = 150, null=True, blank=True)
	f1 = models.CharField(max_length = 150, null=True, blank=True)
	f2 = models.CharField(max_length = 150, null=True, blank=True)
	f3 = models.CharField(max_length = 150, null=True, blank=True)
	f4 = models.CharField(max_length = 150, null=True, blank=True)
	f5 = models.CharField(max_length = 150, null=True, blank=True)
	f6 = models.CharField(max_length = 150, null=True, blank=True)
	f7 = models.CharField(max_length = 150, null=True, blank=True)
	f8 = models.CharField(max_length = 150, null=True, blank=True)

	s0 = models.CharField(max_length = 150, null=True, blank=True)
	s1 = models.CharField(max_length = 150, null=True, blank=True)
	s2 = models.CharField(max_length = 150, null=True, blank=True)
	s3 = models.CharField(max_length = 150, null=True, blank=True)
	s4 = models.CharField(max_length = 150, null=True, blank=True)
	s5 = models.CharField(max_length = 150, null=True, blank=True)
	s6 = models.CharField(max_length = 150, null=True, blank=True)
	s7 = models.CharField(max_length = 150, null=True, blank=True)
	s8 = models.CharField(max_length = 150, null=True, blank=True)

	u0 = models.CharField(max_length = 150, null=True, blank=True)
	u1 = models.CharField(max_length = 150, null=True, blank=True)
	u2 = models.CharField(max_length = 150, null=True, blank=True)
	u3 = models.CharField(max_length = 150, null=True, blank=True)
	u4 = models.CharField(max_length = 150, null=True, blank=True)
	u5 = models.CharField(max_length = 150, null=True, blank=True)
	u6 = models.CharField(max_length = 150, null=True, blank=True)
	u7 = models.CharField(max_length = 150, null=True, blank=True)
	u8 = models.CharField(max_length = 150, null=True, blank=True)

	def __str__(self):
		na = str(str(self.clno) + " " + self.clse + " " + self.cltime)
		return na




class tett(models.Model):
	tid = models.PositiveIntegerField()

	fname = models.CharField(max_length = 150)
	lname = models.CharField(max_length = 150)

	sub1 = models.CharField(max_length = 150, null=True, blank=True)
	sub2 = models.CharField(max_length = 150, null=True, blank=True)

	cla1 = models.PositiveIntegerField()
	se1 = models.CharField(max_length = 10)
	ti1 = models.CharField(max_length = 150)

	cla2 = models.PositiveIntegerField(null=True, blank=True)
	se2 = models.CharField(max_length = 10, null=True, blank=True)
	ti2 = models.CharField(max_length = 150, null=True, blank=True)

	cla3 = models.PositiveIntegerField(null=True, blank=True)
	se3 = models.CharField(max_length = 10, null=True, blank=True)
	ti3 = models.CharField(max_length = 150, null=True, blank=True)

	cla4 = models.PositiveIntegerField(null=True, blank=True)
	se4 = models.CharField(max_length = 10, null=True, blank=True)
	ti4 = models.CharField(max_length = 150, null=True, blank=True)

	cla5 = models.PositiveIntegerField(null=True, blank=True)
	se5 = models.CharField(max_length = 10, null=True, blank=True)
	ti5 = models.CharField(max_length = 150, null=True, blank=True)

	cla6 = models.PositiveIntegerField(null=True, blank=True)
	se6 = models.CharField(max_length = 10, null=True, blank=True)
	ti6 = models.CharField(max_length = 150, null=True, blank=True)

	cla7 = models.PositiveIntegerField(null=True, blank=True)
	se7 = models.CharField(max_length = 10, null=True, blank=True)
	ti7 = models.CharField(max_length = 150, null=True, blank=True)

	m0 = models.CharField(max_length = 150, null=True, blank=True)
	m1 = models.CharField(max_length = 150, null=True, blank=True)
	m2 = models.CharField(max_length = 150, null=True, blank=True)
	m3 = models.CharField(max_length = 150, null=True, blank=True)
	m4 = models.CharField(max_length = 150, null=True, blank=True)
	m5 = models.CharField(max_length = 150, null=True, blank=True)
	m6 = models.CharField(max_length = 150, null=True, blank=True)
	m7 = models.CharField(max_length = 150, null=True, blank=True)
	m8 = models.CharField(max_length = 150, null=True, blank=True)

	t0 = models.CharField(max_length = 150, null=True, blank=True)
	t1 = models.CharField(max_length = 150, null=True, blank=True)
	t2 = models.CharField(max_length = 150, null=True, blank=True)
	t3 = models.CharField(max_length = 150, null=True, blank=True)
	t4 = models.CharField(max_length = 150, null=True, blank=True)
	t5 = models.CharField(max_length = 150, null=True, blank=True)
	t6 = models.CharField(max_length = 150, null=True, blank=True)
	t7 = models.CharField(max_length = 150, null=True, blank=True)
	t8 = models.CharField(max_length = 150, null=True, blank=True)

	w0 = models.CharField(max_length = 150, null=True, blank=True)
	w1 = models.CharField(max_length = 150, null=True, blank=True)
	w2 = models.CharField(max_length = 150, null=True, blank=True)
	w3 = models.CharField(max_length = 150, null=True, blank=True)
	w4 = models.CharField(max_length = 150, null=True, blank=True)
	w5 = models.CharField(max_length = 150, null=True, blank=True)
	w6 = models.CharField(max_length = 150, null=True, blank=True)
	w7 = models.CharField(max_length = 150, null=True, blank=True)
	w8 = models.CharField(max_length = 150, null=True, blank=True)

	h0 = models.CharField(max_length = 150, null=True, blank=True)
	h1 = models.CharField(max_length = 150, null=True, blank=True)
	h2 = models.CharField(max_length = 150, null=True, blank=True)
	h3 = models.CharField(max_length = 150, null=True, blank=True)
	h4 = models.CharField(max_length = 150, null=True, blank=True)
	h5 = models.CharField(max_length = 150, null=True, blank=True)
	h6 = models.CharField(max_length = 150, null=True, blank=True)
	h7 = models.CharField(max_length = 150, null=True, blank=True)
	h8 = models.CharField(max_length = 150, null=True, blank=True)

	f0 = models.CharField(max_length = 150, null=True, blank=True)
	f1 = models.CharField(max_length = 150, null=True, blank=True)
	f2 = models.CharField(max_length = 150, null=True, blank=True)
	f3 = models.CharField(max_length = 150, null=True, blank=True)
	f4 = models.CharField(max_length = 150, null=True, blank=True)
	f5 = models.CharField(max_length = 150, null=True, blank=True)
	f6 = models.CharField(max_length = 150, null=True, blank=True)
	f7 = models.CharField(max_length = 150, null=True, blank=True)
	f8 = models.CharField(max_length = 150, null=True, blank=True)

	s0 = models.CharField(max_length = 150, null=True, blank=True)
	s1 = models.CharField(max_length = 150, null=True, blank=True)
	s2 = models.CharField(max_length = 150, null=True, blank=True)
	s3 = models.CharField(max_length = 150, null=True, blank=True)
	s4 = models.CharField(max_length = 150, null=True, blank=True)
	s5 = models.CharField(max_length = 150, null=True, blank=True)
	s6 = models.CharField(max_length = 150, null=True, blank=True)
	s7 = models.CharField(max_length = 150, null=True, blank=True)
	s8 = models.CharField(max_length = 150, null=True, blank=True)

	u0 = models.CharField(max_length = 150, null=True, blank=True)
	u1 = models.CharField(max_length = 150, null=True, blank=True)
	u2 = models.CharField(max_length = 150, null=True, blank=True)
	u3 = models.CharField(max_length = 150, null=True, blank=True)
	u4 = models.CharField(max_length = 150, null=True, blank=True)
	u5 = models.CharField(max_length = 150, null=True, blank=True)
	u6 = models.CharField(max_length = 150, null=True, blank=True)
	u7 = models.CharField(max_length = 150, null=True, blank=True)
	u8 = models.CharField(max_length = 150, null=True, blank=True)

	def __str__(self):
		na = str(str(self.tid) + " " + self.fname + " " + self.lname)
		return na