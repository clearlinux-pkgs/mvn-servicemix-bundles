#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-servicemix-bundles
Version  : 1.1.4c.6
Release  : 1
URL      : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.jar
Source0  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.jar
Source1  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/bundles-pom/6/bundles-pom-6.pom
Source2  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/bundles-pom/8/bundles-pom-8.pom
Source3  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.jar
Source4  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.pom
Source5  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.jar
Source6  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.pom
Source7  : https://repo1.maven.org/maven2/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-servicemix-bundles-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-servicemix-bundles package.
Group: Data

%description data
data components for the mvn-servicemix-bundles package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/6
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/6/bundles-pom-6.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/8
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/8/bundles-pom-8.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/6/bundles-pom-6.pom
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/bundles-pom/8/bundles-pom-8.pom
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.jar
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.antlr/2.7.7_5/org.apache.servicemix.bundles.antlr-2.7.7_5.pom
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.jar
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.dom4j/1.6.1_5/org.apache.servicemix.bundles.dom4j-1.6.1_5.pom
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.jar
/usr/share/java/.m2/repository/org/apache/servicemix/bundles/org.apache.servicemix.bundles.xpp3/1.1.4c_6/org.apache.servicemix.bundles.xpp3-1.1.4c_6.pom
